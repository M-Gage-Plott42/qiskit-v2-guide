# R3: native-platform inventory and validation procedures

October 31, 2026. **Preparation complete; additional native-platform coverage
remains open.** The user confirmed that no additional host is available and
requested procedures. No Windows or macOS setup/test/UI command below was run.
No infrastructure, environment, package, source archive, or remote session was
created for this preparation.

## Actual access and retained results

The available execution host is **Ubuntu 26.04.1 LTS, Linux x86_64, 64-bit,
kernel 7.0.0-42-generic, glibc 2.43**, with no WSL environment/kernel marker.
The enabled tools expose no additional native host execution service, and no
authorized remote endpoint was supplied. Host inventory did not inspect SSH
credentials/configurations, scan networks, or infer authorization from aliases.

- **Linux x86_64:** retain [R1](R1_FRESH_LINUX_VALIDATION.md)'s fresh-install
  160-test/eight-notebook result and [R2](R2_INTERACTIVE_VALIDATION.md)'s qualified
  Chrome/JupyterLab UI result. All 57 relevant source/test/notebook/runner/pin/
  workflow files match R1 source `9e73b82`; no duplicate Linux run was needed.
- **Windows x64:** untested; no accessible authorized native host.
- **macOS ARM64:** untested; no accessible authorized native host.
- **macOS Intel x86_64:** untested; no accessible authorized native host.
- **Native VS Code/Cursor UI:** separately untested, retaining the R2 access gap.
  Exact Chrome version also remains unverified after R2's browser-policy block.

These are candidate targets, not final classroom support promises. Rick's reply
will determine which platforms matter. Windows ARM64 and 32-bit Python remain
outside the stated target. WSL is Linux evidence, and translated x86_64 on Apple
Silicon is not physical Intel-Mac evidence. Missing hosts are **untested**, not
algorithm failures. No new runtime passes are claimed in this document.

## Preconditions for a future native run

The assistant performs these steps when a real authorized host is available;
the user is not assigned a manual code audit.

1. Identify the actual host OS/build, physical architecture, process architecture,
   available UI surface, and an existing approved CPython 3.12 installation.
   Do not provision a VM/cloud host, install an OS/interpreter/Rosetta, or claim
   emulation as native coverage under this procedure. If a prerequisite is
   missing, record it and leave the affected target untested.
2. Select an exact committed snapshot whose runtime matches the corrected
   160-test baseline. Current inventory source is
   `4c589fd937ad67b9ba27d79a704ed39390c55549`; its runtime matches `9e73b82`.
   Later documentation commits need their own recorded identity. Do not use
   public Grover rc1 or the historical 92-/158-test review ZIP as the corrected
   source. Any future transfer requires its actual authorized destination.
3. Prepare an internal source export and controller-issued `source-receipt.json`:
   exact commit plus a `files` object mapping relative POSIX paths to full-file
   SHA-256 values. Transfer all required source, tests, eight notebooks,
   requirements/constraints, and runners together. Keep credentials/outputs out.
   Verify the receipt's identity against the controller's retained copy before
   trusting its hashes. This is validation staging, not a new student package.
4. Use a new directory with no existing `.venv`; preserve other environments.
   Place logs, the receipt, and the Python snippets below under a new
   `artifacts/r3-<target>/` directory. Snapshot verification excludes only the declared generated `artifacts/` and
   `.venv/` trees (including validator outputs); neither belongs in the payload
   receipt. Other unexpected files fail the inventory check.
5. Use a native terminal. Keep pins unchanged and use pip 26.2.2. Any install or
   runtime failure stops that target's pass claim; retain logs and repair within
   a separately documented scope. Do not silently relax constraints.

The source receipt format is:

```json
{
  "source_commit": "FULL_COMMIT_ID",
  "files": {
    "requirements.txt": "FULL_SHA256",
    "constraints-ci.txt": "FULL_SHA256",
    "src/phys3810/shor.py": "FULL_SHA256"
  }
}
```

The example is abbreviated: a real receipt lists **every exported payload file**.
Verify it before installation and after all checks, using this standard-library
snippet saved as `verify_payload.py` in the evidence directory. The working
directory must be the source root; never manufacture a new expected receipt
from potentially modified files on the target.

```python
from pathlib import Path, PurePosixPath
import hashlib
import json
import sys

root = Path.cwd().resolve()
receipt = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
for relative, expected in receipt["files"].items():
    path = PurePosixPath(relative)
    assert not path.is_absolute() and ".." not in path.parts
    assert "\\" not in relative and ":" not in relative
    assert path.parts[0] not in {"artifacts", ".venv"}
    target = root / relative
    assert target.resolve().is_relative_to(root)
    assert target.is_file() and not target.is_symlink()
    assert hashlib.sha256(target.read_bytes()).hexdigest() == expected, relative
actual = {p.relative_to(root).as_posix() for p in root.rglob("*")
          if p.is_file() and p.relative_to(root).parts[0] not in {"artifacts", ".venv"}}
assert actual == set(receipt["files"]), "Unexpected or missing payload files"
print(f"PASSED: {len(receipt['files'])} payload hashes; {receipt['source_commit']}")
```

## Windows x64 procedure — not executed

Use native PowerShell, not WSL. Confirm physical x64 architecture with CIM,
as well as the Python process being 64-bit Windows. Microsoft's
[processor architecture enumeration](https://learn.microsoft.com/en-us/windows/win32/cimwin32prov/win32-processor)
identifies x64 as 9 and ARM64 as 12. Only record OS/build/architecture fields;
do not collect serial numbers, machine/account identifiers, or credentials.

Save this standard-library precheck as `windows_precheck.py` in the evidence
directory. Using a file avoids differing `python -c` quote handling across
PowerShell versions.

```python
import json
import platform
import struct
import sys

assert sys.platform == "win32" and sys.implementation.name == "cpython"
assert sys.version_info[:2] == (3, 12) and struct.calcsize("P") == 8
assert platform.machine().lower() in ("amd64", "x86_64")
print(json.dumps({"python": sys.version, "executable": sys.executable,
                  "platform": platform.platform(), "process_arch": platform.machine()}, indent=2))
```

Run from the new source root. `py -3.12` refers to the approved existing
interpreter; if unavailable, stop rather than install another one. Direct
invocation avoids changing PowerShell activation policy. The checked wrapper uses
[Start-Process](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.management/start-process)
with separate logs and the returned process exit code; a launch failure throws
instead of reusing a stale native exit code. Its quoting guard covers the fixed
arguments below, including paths with spaces, without inline Python quote parsing.

```powershell
$ErrorActionPreference = 'Stop'
$R3Evidence = Join-Path $PWD 'artifacts\r3-windows-x64'
New-Item -ItemType Directory -Path $R3Evidence -Force | Out-Null
# Place verified source-receipt.json and the documented Python snippets here.

$R3OS = Get-CimInstance Win32_OperatingSystem
$R3CPU = @(Get-CimInstance Win32_Processor)
$R3OS | Select-Object Caption,Version,BuildNumber,OSArchitecture |
    ConvertTo-Json | Set-Content "$R3Evidence\os.json" -Encoding UTF8
$R3CPU | Select-Object Architecture,AddressWidth |
    ConvertTo-Json | Set-Content "$R3Evidence\cpu.json" -Encoding UTF8
if (!$R3CPU.Count -or @($R3CPU | Where-Object {
    $_.Architecture -ne 9 -or $_.AddressWidth -ne 64
}).Count) { throw 'Native Windows x64 host identity not established.' }

function Invoke-R3 {
    param([string]$R3Label, [string]$R3Executable, [string[]]$R3Arguments)
    $R3Resolved = (Get-Command $R3Executable -CommandType Application -ErrorAction Stop).Source
    $R3Quoted = foreach ($R3Argument in $R3Arguments) {
        # All fixed arguments below satisfy this Windows quoting guard.
        if ($R3Argument.Contains('"') -or $R3Argument.EndsWith('\')) {
            throw 'Unsupported argument form; do not improvise native quoting.'
        }
        '"' + $R3Argument + '"'
    }
    $R3Process = Start-Process -FilePath $R3Resolved -ArgumentList ($R3Quoted -join ' ') -WorkingDirectory $PWD.Path -Wait -PassThru -NoNewWindow -RedirectStandardOutput "$R3Evidence\$R3Label.stdout.log" -RedirectStandardError "$R3Evidence\$R3Label.stderr.log" -ErrorAction Stop
    $R3Code = $R3Process.ExitCode
    if ($null -eq $R3Code) { throw 'No native exit code was returned.' }
    $R3Code | Set-Content "$R3Evidence\$R3Label.exit-code" -Encoding ASCII
    if ($R3Code -ne 0) { throw "$R3Label failed with exit $R3Code; retain its logs." }
}

Remove-Item Env:PYTHONPATH,Env:PYTHONHOME -ErrorAction SilentlyContinue
$env:PYTHONNOUSERSITE = '1'
$env:PYTHONDONTWRITEBYTECODE = '1'
$env:OMP_NUM_THREADS = '2'
$env:OPENBLAS_NUM_THREADS = '2'
# Process-local pip isolation; preserve existing user/global config files.
Get-ChildItem Env: | Where-Object { $_.Name -like 'PIP_*' } |
    ForEach-Object { Remove-Item -LiteralPath ('Env:' + $_.Name) }
$env:PIP_CONFIG_FILE = 'nul'
$env:PIP_INDEX_URL = 'https://pypi.org/simple'
$env:PIP_NO_INPUT = '1'
$env:PIP_DISABLE_PIP_VERSION_CHECK = '1'
Remove-Item Env:JUPYTER_PATH,Env:JUPYTER_CONFIG_PATH -ErrorAction SilentlyContinue
$env:JUPYTER_PREFER_ENV_PATH = '1'
foreach ($R3Setting in @('JUPYTER_CONFIG_DIR','JUPYTER_DATA_DIR','JUPYTER_RUNTIME_DIR','IPYTHONDIR','MPLCONFIGDIR','JUPYTERLAB_SETTINGS_DIR','JUPYTERLAB_WORKSPACES_DIR')) {
    $R3Directory = Join-Path $R3Evidence $R3Setting
    New-Item -ItemType Directory -Path $R3Directory -Force | Out-Null
    [Environment]::SetEnvironmentVariable($R3Setting,$R3Directory,'Process')
}
Invoke-R3 precheck py.exe @('-3.12',"$R3Evidence\windows_precheck.py")
Invoke-R3 before-hashes py.exe @('-3.12',"$R3Evidence\verify_payload.py","$R3Evidence\source-receipt.json")
if (Test-Path -LiteralPath '.venv') { throw 'Use a new source export; do not overwrite .venv.' }
Invoke-R3 create-venv py.exe @('-3.12','-m','venv','.venv')
$R3Python = Join-Path $PWD '.venv\Scripts\python.exe'
Invoke-R3 initial $R3Python @("$R3Evidence\capture_initial.py","$R3Evidence\initial-packages.json")
Invoke-R3 pin-pip $R3Python @('-m','pip','install','--upgrade','pip==26.2.2')
Invoke-R3 install $R3Python @('-m','pip','install','--report',"$R3Evidence\pip-install-report.json",'-r','requirements.txt')
Invoke-R3 environment $R3Python @("$R3Evidence\verify_environment.py",$R3Evidence)
Invoke-R3 pip-check $R3Python @('-m','pip','check')
Invoke-R3 unit-tests $R3Python @('-m','unittest','discover','-s','tests','-v')
Invoke-R3 classroom $R3Python @('scripts/validate_classroom.py')
Invoke-R3 after-hashes $R3Python @("$R3Evidence\verify_payload.py","$R3Evidence\source-receipt.json")
```

PowerShell 5.1 may write the OS/CPU JSON with a UTF-8 BOM; receipt readers
should use `utf-8-sig`. Command logs are the native process streams; preserve
and identify their encoding rather than assuming every Windows log is UTF-8.

The validator is the Windows classroom entry point; Bash smoke may be **skipped
with reason** when Bash is not part of the supported Windows setup. Do not
install Bash just to turn that optional host check into a pass.

## macOS ARM64 or Intel procedure — not executed

Treat these as separate targets and receipts. First establish physical host
architecture using the actual Mac's system information, recording only model
and chip/processor family. Select `arm64` only for Apple Silicon or `x86_64`
only for an Intel Mac. If that cannot be established, stop the native claim.

A Python process may be translated independently of the terminal or another
binary. Check `sysctl.proc_translated` **inside the selected Python process**,
not merely by running a different `sysctl` executable. Apple's
[Rosetta documentation](https://developer.apple.com/documentation/apple-silicon/about-the-rosetta-translation-environment)
defines the translation indicator and the absent-key case. The snippet records
an absent key explicitly; on Intel, accept it only with separately verified
Intel hardware. Any other query error leaves architecture verification open.
Save this as `mac_precheck.py` in the evidence directory:

```python
import ctypes
import errno
import json
import platform
import struct
import sys

expected = sys.argv[1]
assert expected in ("arm64", "x86_64")
assert sys.platform == "darwin" and sys.implementation.name == "cpython"
assert sys.version_info[:2] == (3, 12) and struct.calcsize("P") == 8
assert platform.machine() == expected
libc = ctypes.CDLL(None, use_errno=True)
query = libc.sysctlbyname
query.argtypes = [ctypes.c_char_p, ctypes.c_void_p,
                  ctypes.POINTER(ctypes.c_size_t), ctypes.c_void_p, ctypes.c_size_t]
query.restype = ctypes.c_int
value = ctypes.c_int()
size = ctypes.c_size_t(ctypes.sizeof(value))
result = query(b"sysctl.proc_translated", ctypes.byref(value), ctypes.byref(size), None, 0)
error = ctypes.get_errno() if result else 0
assert result == 0 or error == errno.ENOENT, (result, error)
translated = value.value if result == 0 else None
assert translated != 1, "Translated Python is not native target evidence."
assert expected != "arm64" or translated == 0
print(json.dumps({"python": sys.version, "executable": sys.executable,
                  "process_arch": platform.machine(), "expected_arch": expected,
                  "translation_value": translated, "query_result": result,
                  "query_errno": error}, indent=2))
```

Use Bash on the actual Mac and the existing approved `python3.12`. Change the
architecture variable only after identifying the target; do not force another
architecture using Rosetta or emulate a target on Linux.

```bash
set -euo pipefail
unset PYTHONPATH PYTHONHOME
export PYTHONNOUSERSITE=1 PYTHONDONTWRITEBYTECODE=1
export OMP_NUM_THREADS=2 OPENBLAS_NUM_THREADS=2
# Clear only process-local pip overrides, not host configuration files.
for r3_key in $(compgen -e); do
    case "$r3_key" in PIP_*) unset "$r3_key" ;; esac
done
export PIP_CONFIG_FILE=/dev/null PIP_INDEX_URL=https://pypi.org/simple
export PIP_NO_INPUT=1 PIP_DISABLE_PIP_VERSION_CHECK=1
r3_arch=arm64  # Use x86_64 only on a verified Intel Mac.
r3_evidence="$PWD/artifacts/r3-macos-$r3_arch"
mkdir -p "$r3_evidence"
unset JUPYTER_PATH JUPYTER_CONFIG_PATH
export JUPYTER_PREFER_ENV_PATH=1
for r3_setting in JUPYTER_CONFIG_DIR JUPYTER_DATA_DIR JUPYTER_RUNTIME_DIR IPYTHONDIR MPLCONFIGDIR JUPYTERLAB_SETTINGS_DIR JUPYTERLAB_WORKSPACES_DIR; do
    mkdir -p "$r3_evidence/$r3_setting"
    export "$r3_setting=$r3_evidence/$r3_setting"
done
# Place the verified receipt and documented Python snippets here.
r3_run() {
    local r3_label="$1"
    shift
    local r3_code=0
    "$@" >"$r3_evidence/$r3_label.log" 2>&1 || r3_code=$?
    printf '%s\n' "$r3_code" >"$r3_evidence/$r3_label.exit-code"
    return "$r3_code"
}
r3_run os-version sw_vers -productVersion
r3_run os-build sw_vers -buildVersion
r3_run shell-architecture uname -m
r3_run precheck python3.12 "$r3_evidence/mac_precheck.py" "$r3_arch"
r3_run before-hashes python3.12 "$r3_evidence/verify_payload.py" "$r3_evidence/source-receipt.json"
if [ -e .venv ]; then printf '%s\n' 'Use a new source export; .venv exists.' >&2; exit 1; fi
r3_run create-venv python3.12 -m venv .venv
r3_python="$PWD/.venv/bin/python"
export PATH="$PWD/.venv/bin:$PATH"
r3_run initial "$r3_python" "$r3_evidence/capture_initial.py" "$r3_evidence/initial-packages.json"
r3_run pin-pip "$r3_python" -m pip install --upgrade pip==26.2.2
r3_run install "$r3_python" -m pip install --report "$r3_evidence/pip-install-report.json" -r requirements.txt
r3_run environment "$r3_python" "$r3_evidence/verify_environment.py" "$r3_evidence"
r3_run pip-check "$r3_python" -m pip check
r3_run unit-tests "$r3_python" -m unittest discover -s tests -v
r3_run classroom "$r3_python" scripts/validate_classroom.py
r3_run smoke bash scripts/smoke_local.sh
r3_run after-hashes "$r3_python" "$r3_evidence/verify_payload.py" "$r3_evidence/source-receipt.json"
```

Both procedures disable inherited pip redirection/configuration in their new
terminal process, using the platform's null configuration path and explicit
PyPI index. This prevents a pre-existing target/prefix override from installing
outside the fresh venv. Jupyter settings/runtime directories are also isolated
under the new evidence area; kernel registration below still targets the new
venv through `--sys-prefix`. [pip documents this configuration mechanism](https://pip.pypa.io/en/stable/topics/configuration/#pip-config-file).
If an institution requires another approved index, record that decision before
running rather than silently inheriting it. Cache reuse, if any, is compatible
with a fresh installation but must be described accurately.

## Shared initial and post-install evidence

Save this as `capture_initial.py`; both platform procedures run it immediately
after creating `.venv`, before installation. This uses only the standard library.

```python
from pathlib import Path
import importlib.metadata as metadata
import json
import sys

assert sys.prefix != sys.base_prefix
initial = {d.metadata["Name"]: d.version for d in metadata.distributions()}
assert {name.lower().replace("_", "-") for name in initial} <= {"pip", "setuptools"}
Path(sys.argv[1]).write_text(json.dumps(initial, indent=2) + "\n", encoding="utf-8")
```

Save the following as `verify_environment.py`. It writes UTF-8 JSON itself, avoiding shell
redirection encoding differences. Constraint markers must be evaluated on the
actual target. Do not require Linux's 114-package count or install every unused
optional constraint. [Python's venv documentation](https://docs.python.org/3.12/library/venv.html)
explains environment isolation, direct interpreter invocation, and why an
existing environment should be recreated rather than moved.

```python
from pathlib import Path
import importlib.metadata as metadata
import json
import platform
import site
import struct
import sys
from packaging.requirements import Requirement
from packaging.utils import canonicalize_name

root = Path.cwd().resolve()
evidence = Path(sys.argv[1]).resolve()
prefix = Path(sys.prefix).resolve()
assert prefix == (root / ".venv").resolve() and sys.prefix != sys.base_prefix
assert not site.ENABLE_USER_SITE and struct.calcsize("P") == 8
assert sys.implementation.name == "cpython" and sys.version_info[:2] == (3, 12)
config = (prefix / "pyvenv.cfg").read_text(encoding="utf-8")
assert "include-system-site-packages = false" in config
initial = json.loads((evidence / "initial-packages.json").read_text(encoding="utf-8"))
initial = {canonicalize_name(name): version for name, version in initial.items()}
assert set(initial) <= {"pip", "setuptools"}
active = {}
for line in (root / "constraints-ci.txt").read_text(encoding="utf-8").splitlines():
    if not line.strip() or line.startswith("#"):
        continue
    requirement = Requirement(line)
    if requirement.marker is None or requirement.marker.evaluate():
        active[canonicalize_name(requirement.name)] = requirement
installed = {}
for distribution in metadata.distributions():
    name = canonicalize_name(distribution.metadata["Name"])
    location = Path(distribution.locate_file("")).resolve()
    assert location.is_relative_to(prefix), (name, location)
    version = distribution.version
    if name in active:
        assert active[name].specifier.contains(version, prereleases=True), (name, version)
    else:
        assert name in initial, ("unexpected unconstrained package", name)
        assert name == "pip" or version == initial[name]
    installed[name] = {"version": version, "location": str(location)}
assert installed["pip"]["version"] == "26.2.2"
assert "qiskit-ibm-runtime" not in installed
record = {"python": sys.version, "executable": sys.executable,
          "prefix": sys.prefix, "base_prefix": sys.base_prefix,
          "platform": platform.platform(), "machine": platform.machine(),
          "initial_packages": initial, "pyvenv_cfg": config,
          "installed": installed,
          "active_constraint_matches": sorted(set(installed) & set(active)),
          "unused_active_constraints": sorted(set(active) - set(installed))}
(evidence / "environment.json").write_text(json.dumps(record, indent=2) + "\n", encoding="utf-8")
print("PASSED: fresh-environment isolation and active constraints")
```

## Actual UI execution and result audit on each native host

After the native automated checks pass, register the kernel in the **new** venv:

- Windows: `& $R3Python -m ipykernel install --sys-prefix --name phys3810-fa2026 --display-name 'Python (PHYS 3810)'`.
- macOS: `"$r3_python" -m ipykernel install --sys-prefix --name phys3810-fa2026 --display-name 'Python (PHYS 3810)'`.

Record the exit code and kernelspec argv; it must point to that target's new
interpreter. Use a separate working copy for interactive outputs while retaining
the original payload and manifest. Launch that interpreter with `-m jupyterlab`
from the working copy, keep the terminal open, and use actual browser UI.

Explicitly select the named kernel in **each** required notebook; verify printed
interpreter paths where available. Restart/run all, inspect every figure/error,
save the execution copy, shut down JupyterLab, close the tab, relaunch without
reinstallation, and rerun preflight plus a representative lesson. Inspect actual
VS Code/Cursor interpreter and notebook-kernel selection only when that native
UI is available. A matching kernel display name, saved outputs, or headless run
cannot replace these observations. Record browser/editor versions where access
permits; honor access-policy blocks and mark missing facts unverified.

The strict validator must pass **160 tests and eight notebooks**. Separately,
the saved UI execution copies must show **eight notebooks, 50 nonempty code
cells, and 16 PNGs**; UI execution does not rerun the unit suite by itself.
Per-notebook cells/PNGs are preflight 4/2, statevector 3/0, Aer 4/0, Grover 9/3,
QFT 7/2, QPE 8/3, HHL 7/3, Shor 8/3. Check execution counts, no error outputs,
unchanged cell sources/IDs, and all three HHL/Shor figures. Do not infer success
from printed messages alone. Keep source notebooks output-free, executed copies
separate, and preserve partial outputs on failure. UI output auditing corroborates
actual actions; it does not cause execution itself.

## Receipt and completion requirements

For each OS/architecture, the assistant records:

- Actual host authorization/access, OS/build, verified hardware/process
  architectures, and macOS translation result (including absent/error cases).
- Source commit, transfer receipt identity, all payload hashes before/after,
  requirements/constraints hashes, and any scoped repair with new source identity.
- Fresh-directory proof, initial package inventory, pyvenv.cfg, Python/pip paths
  and versions, full installed inventory, active-constraint comparison, and
  installation report. Distinguish fresh packages from reused interpreter/OS.
- Exact commands, native exit codes, stdout/stderr logs, and setup/validator
  outcomes; no fixed Linux package count assumed on other platforms.
- Eight-notebook counts/error/figure audit, actual UI/kernel/reopen evidence,
  browser/editor versions or precise access limitations, and preserved assets.
- Explicit **passed**, **failed**, **skipped with reason**, or **untested** labels
  per automated/UI/editor target. A future package needs its own extraction
  check; this protocol does not create a release or independent model review.

Retain private machine paths/logs/screenshots in local evidence; public docs
contain only technical conclusions and necessary platform facts. Do not include
serial numbers, account identifiers, keys, tokens, or student data. A target is
complete only after its actual automated and claimed UI paths pass. Unavailable
hosts and editor paths remain separate untested entries.

## Current disposition and next work

Inventory/preparation is complete. The user confirmed no additional host;
Windows x64 and both macOS targets remain **untested**, with overall R3 coverage
open pending access and classroom target decisions. Prior Linux evidence carries
forward; its existing R2 editor gap is not closed. The platform commands were
reviewed and Python/Bash snippets checked syntactically on Linux, which is **not
native execution evidence**. No PowerShell execution or syntax pass is claimed.

While Rick's reply and host access remain pending, prepare provisional R4
presenter run sheets and measure local demonstration execution, distinguishing
those measurements from human teaching rehearsal. Do not invent dates, grading,
platform support, or instructor agreement. **GPT Pro sync: not needed now**;
unchanged algorithms and procedure preparation do not need another algorithm
review. The matching PDF/teaching checkpoint remains later work.
