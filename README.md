# TEP — Submer to Examon Telemetry Bridge

A small Python service that collects immersion-cooling telemetry from a
[Submer](https://submer.com/) SmartPod on-prem RESTful API and publishes it to
the [Examon](https://github.com/EEESlab/examon) monitoring system over MQTT.

The service runs continuously, polling the Submer SmartPod for **live**,
**average**, and **configuration** data at regular intervals and forwarding each
metric to Examon as MQTT topics.

## What it does

- **Collects** SmartPod immersion-cooling metrics from the Submer on-prem REST
  API — coolant/water temperatures and flow, power consumption, heat
  dissipation, mPUE (energy-efficiency ratio), pump status/RPM, CPU
  temperatures, and active/fixed errors and warnings.
- **Transforms** the JSON payload into the Examon data model, mapping each
  measurement to a hierarchical MQTT topic under `org/tep/submer/...`.
- **Publishes** the transformed metrics to an MQTT broker consumed by Examon.

Because a live Submer SmartPod is not always available, the project also ships a
FastAPI mock server (`data_gen.py`) that generates realistic dummy telemetry for
local testing.

## Data flow

```
Submer SmartPod REST API  ──►  submer_collector.py  ──►  examon_collector.py  ──►  examon_publisher.py  ──►  MQTT broker ──► Examon
   (or data_gen.py mock)         (fetch live/avg/cfg)     (JSON → Examon model)      (paho-mqtt publish)
```

## Requirements

- Python 3.12
- [Poetry](https://python-poetry.org/)
- An MQTT broker reachable by `examon_publisher.py`

## Installation

```sh
git clone https://github.com/MSKazemi/tep.git
cd tep
poetry install
```

## Usage

Start the FastAPI mock Submer API (optional, for local testing):

```sh
poetry run python data_gen.py
```

Run the collector/publisher loop:

```sh
poetry run python main.py
```

`main.py` collects live, average, and configuration data from the Submer API and
publishes the live data to the MQTT broker every 60 seconds.

## Project structure

```
.
├── main.py               # Entry point: collect and publish on a loop
├── submer_collector.py   # Fetch live / average / configuration data from the Submer API
├── examon_collector.py   # Convert Submer JSON into the Examon data model (MQTT topics)
├── examon_publisher.py   # Publish the Examon-formatted metrics to an MQTT broker
├── data_gen.py           # FastAPI mock server that generates dummy Submer telemetry
├── pyproject.toml        # Poetry project and dependencies
├── poetry.lock
└── tests/
```

## Configuration

- **Submer API endpoint** — `submer_collector.py` targets
  `http://127.0.0.1:8000` by default (the address of the `data_gen.py` mock).
  Point it at a real SmartPod to collect live data.
- **MQTT broker** — configure the broker host, port, and credentials in
  `examon_publisher.py`.

## Key concepts

- **Submer SmartPod** — an immersion (liquid) cooling unit for data-center and
  HPC hardware; it exposes an on-prem RESTful API for telemetry.
- **Examon** — an open monitoring framework for HPC systems and data centers
  that ingests metrics over MQTT.
- **mPUE** — a Submer-reported energy-efficiency ratio included in the telemetry.

## License

The project header declares the MIT License. No `LICENSE` file is currently
included in the repository.

<!-- legal-notice: start -->
### Legal notice and responsible use

The materials in this repository are made available without warranties to the extent permitted by applicable law. **Please read the [Disclaimer and Responsible-Use Notice](DISCLAIMER.md)** before relying on or deploying them. This notice does not change any existing software license or limit rights that cannot legally be waived.
<!-- legal-notice: end -->

<!-- risk-guidance: start -->
### Operational safety and limitations

Before connecting accounts, running automation, relying on consequential outputs, or using production systems, review [project-specific safety risks and pre-deployment checks](SAFETY.md). The checklist describes precautions to **verify**, not a certification that the software currently enforces every safeguard.
<!-- risk-guidance: end -->

<!-- licensing-status: start -->
### Licensing and reuse status

**No repository-root license has yet been confirmed for this project.** Read [Rights and Licensing Status](LICENSING_STATUS.md) before copying, redistributing, or adapting code or content. A public repository and its disclaimer do not by themselves grant new reuse permissions. Existing valid third-party rights and licenses remain in effect.
<!-- licensing-status: end -->

<!-- security-reporting: start -->
### Security reporting

Please follow the [security policy](SECURITY.md) to report suspected vulnerabilities privately. Avoid disclosing credentials or exploitable details in public issues.
<!-- security-reporting: end -->
