# Safety, limitations and pre-deployment checks — tep

**Scope:** Continuous Submer immersion-cooling telemetry collection and MQTT publishing to Examon.  
**Issued:** 2026-10-17  
**Status:** Risk guidance only. No claim is made that any checklist item is already implemented, tested, legally approved or certified.

This document supplements [DISCLAIMER.md](DISCLAIMER.md) and the existing copyright/license terms without changing either. It does not prevent claims or waive mandatory legal duties.

## Risks to assess

- Stale, missing or malformed temperature, flow and pump telemetry may be mistaken for current physical readings.
- Unexpected API behavior, MQTT connectivity loss or hardcoded endpoints can result in incomplete monitoring.
- Experimental code should not be treated as a certified coolant flow, fire prevention or thermal protection controller.

## Checks before live use

- [ ] Test stale-data detection, sensor fault handling, timeouts, authentication and broker outages.
- [ ] Use read-only vendor API credentials where possible and secure MQTT transport and topic permissions.
- [ ] Validate units, timestamps and device identities against reference sensors in a test environment.
- [ ] Maintain independent hardware safety interlocks and qualified human monitoring for critical thermal systems.

## User and maintainer responsibilities

Begin in an isolated, authorized test environment; apply least privilege, backups, monitoring and an independent review of any high-impact outputs or actions. Where a project depends on third-party providers or real equipment, comply with vendor terms and safety instructions. Report suspected security flaws privately. Record actual test evidence, versions and unresolved risks rather than inferring that documentation is proof of implementation.

**Mandatory rights preserved:** Liability, product-safety, privacy, security and consumer obligations cannot be eliminated by this notice where applicable law forbids exclusion.
