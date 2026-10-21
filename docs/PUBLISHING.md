# Publishing the generated Super Market Python SDK

This repository contains a Scalar-generated client. The Python **distribution**
is `super-market`, its **import package** is `super_market`, and its currently
declared version is `0.1.0` (`pyproject.toml`). Do not confuse the distribution
name with the GitHub repository name (`super-market-api`).

## One-time setup before first public upload

1. Merge the PR introducing `.github/workflows/ci.yml` and
   `.github/workflows/publish-pypi.yml` into `main`.
2. In GitHub repository **Settings > Environments**, create an environment
   named exactly `pypi`. Prefer a deployment policy limited to version tags
   (`v*`) and protection/approval rules if available for your GitHub plan.
3. Sign in at https://pypi.org/ and verify ownership/availability of the
   name **`super-market`**. If it belongs to someone else or is unavailable,
   choose a unique name, then change `pyproject.toml`, the README installation
   command, and the release workflow's PyPI project URL **before publishing**.
4. For the first release of a new PyPI project, open your account's
   **Publishing > Add a new pending publisher** page:
   https://pypi.org/manage/account/publishing/
   Enter the **exact** values:

   | Field | Value |
   | --- | --- |
   | PyPI project name | `super-market` |
   | GitHub owner | `kyle-nguyennn` |
   | GitHub repository name | `super-market-api` |
   | Workflow filename | `publish-pypi.yml` |
   | Environment name | `pypi` |

   If the package already exists **under your own PyPI account**, instead
   configure the publisher at that project's **Manage > Publishing** page.
   Pending publishers do not reserve a package name until first upload.

**No PyPI API token or password is needed**. The release workflow uses
`id-token: write` in the publish job only and `pypa/gh-action-pypi-publish`
to exchange GitHub OIDC identity for temporary publishing credentials.

## First release

Ensure the version in `pyproject.toml` is `0.1.0`. After merging the PR:

```bash
git checkout main
git pull --ff-only origin main
git tag v0.1.0
git push origin v0.1.0
```

The pushed tag triggers **Publish Python SDK to PyPI**, which:

1. Rejects tags not matching `v<major>.<minor>.<patch>`.
2. Rejects tags whose version differs from `pyproject.toml`.
3. Rejects commits that are not ancestors of current `main`.
4. Builds both wheel and source distribution and runs `twine check`.
5. Installs the wheel and verifies the public import without network API calls.
6. Transfers the built files to a separate **OIDC-only** publish job.

Track progress at the repository's **Actions** tab. If the PyPI environment
uses manual reviewers, approve the pending deployment there.

Verify after the workflow succeeds:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install 'super-market==0.1.0'
python -c 'from super_market import SuperMarketAPI; print("import OK")'
```

The package release will be visible at https://pypi.org/project/super-market/
once successfully published. First publication is **public and irreversible**
in the sense that uploaded release files cannot be overwritten.

## Subsequent versions

Update **both** `pyproject.toml` (`[project].version`) and
`src/super_market/_version.py` (`__version__`) to the same new value.
Merge and push a new tag, e.g. `v0.1.1`. Never reuse an existing version
number; PyPI does not allow replacing previously uploaded files.

Scalar regeneration can overwrite generated files including the version.
Review changes to client models, metadata, README, import paths and retry
semantics before tagging. Never publish straight from an unreviewed SDK
regeneration branch.

## Important SIG trading-safety caveat

`tests/smoke-test.py` is a **generated live API smoke runner** that invokes
mutating endpoints including order placement, cancellation and market
creation. Do not invoke it in CI or on a production participant account.

Scalar's SDK supports retries and defaults to `max_retries=2`. For any
authenticated SIG **trading** client, construct the SDK with
`max_retries=0` and keep durable idempotency, exchange state
reconciliation, trade gating, and explicit retry policy inside the
`market-maker` SIG venue facade. SDK build success is not proof of
safe order execution or tournament eligibility.

## Keeping the dependency venue-specific

After the first PyPI release succeeds, add the pinned distribution to
`kyle-nguyennn/market-maker` **only** in
`requirements/sig_predictions.txt` and its SIG-specific Conda environment,
not `requirements/common.txt` or `requirements/hyperliquid.txt`.
Keep the existing SIG adapter and its read-only-by-default order safety guard.
