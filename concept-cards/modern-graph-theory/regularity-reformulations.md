---
concept: Reformulations of Szemerédi's Lemma
slug: regularity-reformulations
category: regularity-method
subcategory: fundamental-theorems
tier: advanced
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Extremal Problems"
chapter_number: 4
pdf_page: 110
section: "IV.5 Szemerédi's Regularity Lemma"
extraction_confidence: high
aliases:
  - "Theorem 29'"
  - "Theorem 29''"
prerequisites:
  - szemeredis-regularity-lemma
extends:
  - szemeredis-regularity-lemma
related: []
contrasts_with: []
answers_questions:
  - "What are equivalent formulations of the regularity lemma?"
---

# Quick Definition
The regularity lemma has equivalent formulations: one with nearly equal classes (no exceptional class), and one with a small exceptional class and strict equality of non-exceptional classes.

# Core Definition
**Theorem 29'**: Every graph has a partition $V = \bigcup_{i=1}^k C_i$ with $m \le k \le M'$, $|C_1| \le |C_2| \le \cdots \le |C_k| \le |C_1|+1$, and all but $\varepsilon k^2$ pairs are $\varepsilon$-uniform.

**Theorem 29''**: Every graph has a partition $V = \bigcup_{i=0}^k C_i$ with $m \le k \le M''$, $|C_0| \le k-1$, $|C_1| = \cdots = |C_k|$, and all but $\varepsilon\binom{k}{2}$ pairs are $\varepsilon$-uniform (Bollobás, pp. 146-147).

# Prerequisites
- **Szemerédi's regularity lemma** — These are equivalent formulations

# Key Properties
1. Theorem 29' avoids an exceptional class by allowing class sizes to differ by 1
2. Theorem 29'' has very small exceptional class ($|C_0| \le k-1$)
3. All three formulations are equivalent
4. Theorem 29'' is most commonly used in applications

# Context & Application
Different formulations are convenient for different applications. Theorem 29'' is used in Section IV.6.

# Examples
**Example** (pp. 146-147): The proofs of equivalence are left as Exercise 60.

# Relationships
## Builds Upon
- **szemeredis-regularity-lemma** — Equivalent forms

# Source Reference
Chapter IV, Section IV.5, pages 146-147. Theorems 29', 29''.

# Verification Notes
- Definition source: Direct from pp. 146-147
- Confidence rationale: Explicitly stated
- Uncertainties: None
- Cross-reference status: Verified
