---
# === CORE IDENTIFICATION ===
concept: Erdos Lower Bound for Ramsey Numbers
slug: erdos-lower-bound-ramsey

# === CLASSIFICATION ===
category: probabilistic-method
subcategory: ramsey-theory
tier: intermediate

# === PROVENANCE ===
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Random Graphs"
chapter_number: 7
pdf_page: 225
section: "VII.1 The Basic Models—The Use of the Expectation"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - Erdos probabilistic lower bound for R(s,s)

# === TYPED RELATIONSHIPS ===
prerequisites:
  - expectation-method
  - subgraph-count-expectation
  - gnp-model
extends:
  - probabilistic-method
related:
  - stirlings-formula
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I use the probabilistic method to prove graph existence results?"
  - "What is the best known lower bound for diagonal Ramsey numbers?"
---

# Quick Definition

Erdos proved $R(s, s) > \frac{1}{e\sqrt{2}} s \cdot 2^{s/2}$ by showing that the expected number of $K_s$ and independent $s$-sets in $\mathcal{G}(n, 1/2)$ is less than 1 for appropriate $n$.

# Core Definition

**Theorem 2** (Bollobás, p. 225): (i) If $3 \le s \le n$ and $\binom{n}{s} < 2^{\binom{s}{2}-1}$, then $R(s,s) \ge n+1$. Also, $R(s,s) > \frac{1}{e\sqrt{2}} s \cdot 2^{s/2}$. (ii) More generally, if $\binom{n}{s}p^{\binom{s}{2}} + \binom{n}{t}q^{\binom{t}{2}} < 1$ then $R(s,t) \ge n+1$. The proof considers $\mathcal{G}(n, 1/2)$ and notes $\mathbb{E}_{1/2}(X_s + X_s') = 2\binom{n}{s}2^{-\binom{s}{2}} < 1$, so some graph has no $K_s$ and no independent set of order $s$.

# Prerequisites

- **Expectation method** -- The first moment method is the proof technique
- **Subgraph count expectation** -- Need $\mathbb{E}(X_s)$ and $\mathbb{E}(X_s')$
- **G(n,p) model** -- The probability space $\mathcal{G}(n, 1/2)$

# Key Properties

1. Gives exponential lower bound: $R(s,s) > c \cdot s \cdot 2^{s/2}$
2. Combined with Erdos-Szekeres upper bound: $2^{s/2} \le R(s,s) \le 2^{2s}$
3. The constant $c = 1/(e\sqrt{2})$ can be improved to $\sqrt{2}/e$ via the Lovasz local lemma
4. It is not known whether the exponent 1 of $s$ can be improved

# Construction / Recognition

## Proof Outline
1. In $\mathcal{G}(n, 1/2)$, compute $\mathbb{E}(X_s + X_s') = 2\binom{n}{s}2^{-\binom{s}{2}}$
2. For $n = \lfloor \frac{s 2^{s/2}}{e\sqrt{2}} \rfloor$, use Stirling's formula to verify this is $< 1$
3. Therefore some graph on $n$ vertices has neither $K_s$ nor $\overline{K_s}$
4. Hence $R(s,s) \ge n + 1$

# Context & Application

This was one of the first applications of the probabilistic method and remains one of its most celebrated. The proof is strikingly simple yet the bound has resisted significant improvement for over 70 years, highlighting the power of probabilistic arguments.

# Examples

**Example** (p. 226): For off-diagonal Ramsey numbers $R(3, t)$, it is now known that $\frac{c_1 t^2}{\log t} \le R(3, t) \le \frac{c_2 t^2}{\log t}$, with the lower bound by Kim (1995) and upper bound by Shearer (1983).

# Relationships

## Builds Upon
- **Expectation method** -- Core proof technique
- **Subgraph count expectation** -- Key computation
- **Stirling's formula** -- Used to estimate binomial coefficients

## Enables
- Further research on Ramsey number bounds

## Related
- **Probabilistic method** -- Paradigmatic example

## Contrasts With
- None

# Common Errors

- **Error**: Attempting to construct the graph explicitly from the probabilistic argument
  **Correction**: The proof is non-constructive; no explicit graph achieving the bound is known for large $s$

# Common Confusions

- **Confusion**: Thinking the bound $R(s,s) > c \cdot s \cdot 2^{s/2}$ is known to be tight
  **Clarification**: The true order of $R(s,s)$ is unknown; it lies between $2^{s/2}$ and $2^{2s}$ (up to polynomial factors)

# Source Reference

Chapter VII: Random Graphs, Section VII.1, Theorem 2, pages 225--226.

# Verification Notes

- Definition source: Direct from Theorem 2, p. 225
- Confidence rationale: Explicit theorem statement with complete proof
- Uncertainties: None
- Cross-reference status: Verified
