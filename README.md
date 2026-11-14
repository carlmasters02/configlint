# configlint

Validates YAML deploy manifests submitted by users before they reach the cluster.

```bash
pip install -r requirements.txt
echo "service: api\nimage: x\nreplicas: 2" | python -m configlint.cli
pytest -q
```
