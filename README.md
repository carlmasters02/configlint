# configlint

> ⚠️ **Intentionally vulnerable.** This repo is the demo target for **[PatchSwarm](https://github.com/carlmasters02/patch-swarm)**. Don't use it in production.

configlint is a tiny Python tool that validates YAML deploy manifests submitted by users (`service`, `image`, `replicas`) before they reach a cluster.

It's built to look like a typical older project that nobody has kept up to date. It pins old dependency versions and parses untrusted input unsafely.

## The planted vulnerability

| | |
|---|---|
| **CVE** | [CVE-2020-14343](https://github.com/advisories/GHSA-8q59-q68h-6hv4): PyYAML arbitrary code execution |
| **Where** | `configlint/loader.py`: `yaml.load(text, Loader=yaml.FullLoader)` |
| **Why it's exploitable** | `requirements.txt` pins `PyYAML==5.3.1`. Before 5.4, `FullLoader` can build arbitrary Python objects, so a crafted manifest can run code on the machine that validates it. |
| **Fix** | `yaml.safe_load(text)` and `PyYAML>=6.0.2` |

`requests==2.25.1` also has known CVEs. A scanner will flag them, but no proof-of-concept here shows them to be reachable. That contrast is the point of the demo: a scanner reports 5 CVEs, and PatchSwarm proves that **1** is exploitable and fixes only that one.

## What PatchSwarm does with this repo

1. Finds the 5 dependency CVEs.
2. Runs a real exploit against `load_manifest()` in a Daytona sandbox and proves CVE-2020-14343 executes code.
3. Pushes the fix to the branch `patchswarm/cve-2020-14343`.
4. Re-runs the exploit on that branch: it's blocked, and the tests below still pass.
5. Has a Qwen model on Nosana review the diff, then opens a PR once a human approves.

## Run it

```bash
pip install -r requirements.txt
printf 'service: api\nimage: x\nreplicas: 2\n' | python -m configlint.cli   # no output = valid
pytest -q                                                                  # 3 tests
```
