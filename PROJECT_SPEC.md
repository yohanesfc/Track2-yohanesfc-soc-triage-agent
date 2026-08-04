# Project Specification Document — Private SOC Triage Agent

Track 2: Development & Local Deployment of Private AI Agents

## 1. Application scenarios

TODO: describe the concrete scenario(s). Draft:
- A security analyst receives a flood of alerts from Wazuh (host-based
  intrusion detection), Suricata (network IDS/IPS), and Greenbone
  (vulnerability scanning). Manual triage is slow and inconsistent.
- The agent ingests alerts, correlates them against MITRE ATT&CK techniques
  and known CVEs, and produces a prioritized, explained triage recommendation
  — entirely on local infrastructure, since security telemetry should not
  leave the network.

## 2. Agent architecture diagram

TODO: insert diagram (see docs/architecture.png). Summary:
Security tools + knowledge base -> agent orchestrator (tool calls, planning,
memory, permissions) -> local LLM on Radeon GPU (vLLM) -> analyst interface.

## 3. Introduction to core capabilities

Capabilities implemented (minimum 2 of 5 required by the track):

- [ ] Local knowledge retrieval (RAG) — MITRE ATT&CK + CVE corpus
- [ ] Tool invocation — Wazuh / Suricata / Greenbone API calls
- [ ] Multi-step task planning — alert -> enrich -> correlate -> recommend
- [ ] Local multi-turn memory — conversation context across analyst turns
- [ ] Permission control & privacy protection — role-based data visibility

TODO: check boxes as implemented, add 2-3 sentences per capability.

## 4. Model introduction & local deployment plan

- Base model: TODO (e.g. Qwen3-8B-Instruct)
- Fine-tuning: TODO (QLoRA cybersecurity fine-tune, if used — describe data
  and training setup)
- Serving: vLLM, OpenAI-compatible API, served locally on AMD Radeon GPU
- Deployment: `vllm serve <model> --host 0.0.0.0 --port 8000` on Radeon Cloud
  instance (ROCm 6.x)

## 5. Optimization description for inference speed on AMD Radeon GPU

TODO after benchmarking. Cover:
- Quantization approach used (if any) and measured speed/quality tradeoff
- Batching / KV-cache settings tuned for Radeon
- Before/after latency and throughput numbers
- Any ROCm-specific tuning applied

---
*Fill in each TODO before submission. Keep this document in sync with
README.md and the demo video script.*
