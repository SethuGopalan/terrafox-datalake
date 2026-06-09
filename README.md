# Terrafox Data Lake Connector
A simple, secure wrapper module to stream files out of your private data lake into remote notebook runtimes seamlessly.

# terrafox-datalake

A lightweight, universal, stream-native connector wrapper designed to stream datasets securely from private MinIO and S3-compatible Data Lakes straight into Pandas dataframes. 

By replacing traditional file-system directory mapping wrappers (`s3fs`/`fsspec`) with direct object streaming via `boto3`, this package completely eliminates network edge bottlenecks, Cloudflare proxy payload limits, and 403 Forbidden credential collisions caused by background directory scanning.

---

## Key Features

- **Stream-Native Engine:** Reads multi-gigabyte datasets (e.g., 1.3 GiB+ CSVs) linearly using high-performance byte-stream network chunks, keeping your local or Google Colab memory consumption minimal.
- **Bypasses Proxy Blocks:** Sidesteps standard reverse-proxy constraints (like Cloudflare Tunnel 100 MiB Client Max Body Size upload blocks) during active read cycles.
- **Fully Universal & Repurposable:** Zero hardcoded endpoints. Works natively out-of-the-box with your configured defaults or targets any custom local/cloud data lake clusters dynamically.
- **Zero Configuration Conflict:** Completely abstracts complex `botocore` configuration arguments, address styling structures, and signature parameters out of your notebooks.

---

## Installation

Install the package directly via pip:

```bash
pip install terrafox-datalake

Quick Start
1. Connecting Natively via Interactive Prompt
If no background credentials are found, calling connect() will safely prompt you for your data lake root credentials:

import terrafox_datalake as dl

# Initializes the data lake client context securely
dl.connect()

2. Silent Credentials Injection (Automated Workflows)
For automated scripts, headless runners, or to bypass the interactive login prompt in Google Colab, cache your environment credentials right before initializing:

import os
import terrafox_datalake as dl

# Pre-populate session data 
os.environ["MINIO_USER"] = "admin"
os.environ["MINIO_PASSWORD"] = "your_secure_password"
os.environ["MINIO_ENDPOINT"] = "[https://minio.terrafoxai.com](https://minio.terrafoxai.com)" # Target endpoint

dl.connect()
3 Advanced Usage: Reusing for Different Infrastructures
This package is completely dynamic. You can reuse the exact same library to switch contexts between production clusters, staging buckets, or local development environments instantly:

import terrafox_datalake as dl

# Explicitly override destination to an alternate cluster or local port mapping
dl.connect(endpoint="[https://local-testing-cluster.local:9000](https://local-testing-cluster.local:9000)")

# Pull rows out of an completely separate infrastructure target
df = dl.read_csv(bucket="test-bucket", key="metrics.csv")

Architecture Requirements

Python: >= 3.7

Dependencies: pandas, boto3
