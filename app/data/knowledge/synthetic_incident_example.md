# Synthetic Incident: Status Lookup Delay

Incident ID: DEMO-INC-0042
Application: PolicyAdmin
Category: Read-only lookup
Symptoms: Status lookup requests took longer than the expected response window.
Root cause: A fictional downstream dependency was responding slowly.
Resolution: Operations verified dependency health and followed the documented retry and escalation policy.
Verification: A read-only status lookup completed successfully and was checked in the source system.
Status: Resolved
