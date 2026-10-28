# Icarus — Roadmap to Research Engineer (Anthropic / OpenAI)

**Start:** October 2026 · **Pace:** ~8 h/week · **Horizon:** 24–30 months
**Starting profile:** software dev, no ML. Chile, willing to relocate.

Weekly rhythm: 5 h course/implementation (writing code) · 2 h paper + notes · 1 h writing in public.
Rule: **every month leaves something public** (repo or post). Mark `[x]` when done.

---

## Phase 1 — Foundations (Oct 2026 – Mar 2027)

### Month 1 · Oct 2026
- [x] Local setup: Python (`uv`), PyTorch with CUDA ≥12.8 (RTX 5070 Laptop 8 GB, Blackwell → `--index-url https://download.pytorch.org/whl/cu128`), public GitHub repo `icarus`
- [ ] 3Blue1Brown — Essence of Linear Algebra (complete)
- [ ] Karpathy Zero to Hero #1: micrograd (reimplemented without looking)
- **Checkpoint:** own micrograd trains an MLP on `make_moons` with ≥95% accuracy

Week by week (if behind, cut 3B1B, not micrograd; leftovers move to the 1st week of Nov):
- **W1 · Oct 12–18:** setup (2 h) · 3B1B ch. 1–5 (2.5 h) · micrograd: derivatives and `Value` class (2.5 h) · repo README (1 h). Done when `torch.cuda.is_available()` returns `True` and the repo is published.
- **W2 · Oct 19–25:** 3B1B ch. 6–9; 10–11 optional (2.5 h) · rest of the video, then close it and rewrite `Value` + `backward()` from memory (5 h). Done when `test_value.py` (written by you) compares your gradients against `torch.autograd` and passes.
- **W3 · Oct 26–Nov 1:** 3B1B ch. 12–16, prioritizing eigenvalues (2.5 h) · `Neuron`/`Layer`/`MLP`, training loop on `make_moons` and decision boundary plot (4.5 h) · push and short post with the plot (1 h).
- **Anti-cheat rule:** watch the video once. If you get stuck, look only at the line blocking you and write down in `NOTES.md` what you didn't understand (material for post #1).

### Month 2 · Nov 2026
- [ ] 3Blue1Brown — calculus + "Neural Networks" (backprop)
- [ ] Zero to Hero #2–3: makemore (bigrams, MLP)
- **Checkpoint:** you can derive backprop by hand for a 2-layer MLP

### Month 3 · Dec 2026
- [ ] Zero to Hero #4–5: activations, BatchNorm, manual backprop ("becoming a backprop ninja")
- [ ] Basic probability: distributions, maximum likelihood, cross-entropy
- **Checkpoint:** post #1 — "what I learned implementing backprop by hand"

### Month 4 · Jan 2027
- [ ] Zero to Hero #6: WaveNet
- [ ] PyTorch in depth: tensors, broadcasting, autograd, `nn.Module`, DataLoader (d2l.ai as reference)
- **Checkpoint:** clean training loop from scratch with logging (wandb) and checkpoints

### Month 5 · Feb 2027
- [ ] Zero to Hero #7: "Let's build GPT"
- [ ] Paper: *Attention Is All You Need*
- **Checkpoint:** own mini GPT trained

### Month 6 · Mar 2027
- [ ] Zero to Hero #8–9: tokenizer (BPE), reproduce GPT-2 124M (GPU rented by the hour: RunPod/Lambda/Vast; on 8 GB it's very slow)
- [ ] Train a GPT on a Spanish corpus
- **Phase 1 checkpoint:** repo + post #2 with a Spanish GPT from scratch

---

## Phase 2 — LLMs from the inside (Apr 2027 – Dec 2027)

Backbone: **Stanford CS336 — Language Modeling from Scratch** (public videos + assignments).
⚠️ Each assignment is designed for full-time students; at 8 h/week it may take 1.5–2 months. If it runs long, the realistic horizon is 30 months, not 24.

### Month 7–8 · Apr–May 2027
- [ ] CS336 A1: BPE tokenizer + transformer + optimizer from scratch
- [ ] Papers: GPT-2, GPT-3 (method sections)
- **Checkpoint:** A1 passes the official tests

### Month 9 · Jun 2027
- [ ] CS336 A2: systems — profiling, FlashAttention in Triton, DDP (DDP requires rented multi-GPU)
- [ ] The Ultra-Scale Playbook (Hugging Face): data/tensor/pipeline parallelism, FSDP
- **Checkpoint:** post #3 — FSDP explained with my own diagrams

### Month 10 · Jul 2027
- [ ] CS336 A3: scaling laws
- [ ] Papers: Kaplan et al. 2020, Chinchilla
- **Checkpoint:** reproduce a scaling curve at small scale

### Month 11 · Aug 2027
- [ ] CS336 A4: data (filtering, dedup)
- [ ] Inference: KV cache, batching, quantization; read vLLM code (PagedAttention)
- **Checkpoint:** take part in the nanoGPT speedrun (or reproduce a record)

### Month 12–13 · Sep–Oct 2027
- [ ] CS336 A5: alignment — SFT, DPO, RL (GRPO)
- [ ] Papers: InstructGPT, Constitutional AI, DPO, DeepSeek-R1
- [ ] Lilian Weng's blog: RLHF, reward hacking
- **Checkpoint:** DPO/GRPO fine-tune of a 0.5–1B model (Qwen) with measured improvement

### Month 14–15 · Nov–Dec 2027
- [ ] Evals: `inspect_ai` (UK AISI), build my own benchmark
- [ ] Read Anthropic's Responsible Scaling Policy + recent model cards
- **Phase 2 checkpoint:** fine-tune repo + own evals + post #4

---

## Phase 3 — Specialization and visibility (Jan 2028 – Dec 2028)

Chosen area (decide in Jan 2028): `____________` (recommended: **evals** or **training infra**)

### Month 16–18 · Jan–Mar 2028
- [ ] ARENA curriculum (transformers, interpretability, RL, evals)
- [ ] Apply: **Anthropic Fellows Program**, **MATS** (check cohort dates)
- **Checkpoint:** first PR accepted in vLLM / TransformerLens / inspect_ai / torchtitan

### Month 19–21 · Apr–Jun 2028
- [ ] Replicate 1 paper in the chosen area, publish results (blog / LessWrong / Alignment Forum)
- [ ] Join communities: EleutherAI Discord, AI safety events
- **Checkpoint:** replication published

### Month 22–24 · Jul–Sep 2028
- [ ] Small original project in the area (something nobody has published)
- [ ] 2–3 additional OSS PRs
- **Phase 3 checkpoint:** portfolio = GPT from scratch + fine-tune/evals + replication + original project + PRs

---

## Phase 4 — Apply (Oct 2028 →)

- [ ] Anthropic-style interview practice: 60–90 min multi-stage Python problems, clean code under pressure (1/week)
- [ ] ML review for interviews: transformers, optimization, distributed, post-training
- [ ] Form my own view on safety (RSP, alignment) for the culture conversation
- [ ] Get referrals (MATS/Fellows, OSS, communities)
- [ ] Apply: Anthropic, OpenAI (SF and **London** — Skilled Worker visa is simpler)
- [ ] Plan B / stepping stone: ML engineer at an AI startup, UK AISI
- [ ] Evaluate O-1 (US) with the accumulated portfolio

---

## Accelerator: current job (Buydepa)
- [ ] Propose and lead an **evals** project on Buydepa's LLM uses (propose around Month 12–14, once grounded in evals and fine-tuning)
- [ ] Fine-tuning or agents with rigorous metrics in production
- Goal: have part of the learning count as professional experience (saves 6–12 months)

---

## Progress log
| Date | What I did | Link |
|------|------------|------|
| 2026-10-12 | Plan revised: local setup (RTX 5070), Month 1 weekly breakdown, notes on rented GPU and CS336 pace | — |
| 2026-10-13 | Repo translated to English; verified PyTorch 2.11 + cu128 sees the RTX 5070; repo published | [veglos/icarus](https://github.com/veglos/icarus) |
| 2026-10-14 | micrograd: `Value` with `+`, `*`, parent graph and `grad`, written from memory · local `_backward` rules for `+` and `*` · 3B1B ch. 1 | — |
| 2026-10-16 | Watched 3B1B NN ch. 3–4 (backprop) | — |
| 2026-10-19 | micrograd: `backward()` via topological sort, written without the video · verified on a shared inner node (`f = d * e`) | — |
| 2026-10-28 | Finished watching Zero to Hero #1 (micrograd) end to end | — |
