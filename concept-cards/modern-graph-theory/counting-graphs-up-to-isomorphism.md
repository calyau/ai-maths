---
# === CORE IDENTIFICATION ===
concept: Counting Graphs up to Isomorphism
slug: counting-graphs-up-to-isomorphism

# === CLASSIFICATION ===
category: graph-enumeration
subcategory: graph-counting
tier: intermediate

# === PROVENANCE ===
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Graphs, Groups and Matrices"
chapter_number: 8
pdf_page: 284
section: "VIII.4 Enumeration and Pólya's Theorem"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - unlabelled graph counting

# === TYPED RELATIONSHIPS ===
prerequisites:
  - polya-enumeration-theorem
  - group-orbit
extends: []
related:
  - cayley-formula-trees
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I count graphs up to isomorphism?"
---

# Quick Definition

Counting graphs up to isomorphism amounts to counting orbits of $\{0,1\}^{V^{(2)}}$ under the permutation group $\Gamma_n$ induced by $S_n$ on vertex pairs, solved in principle by Polya's theorem.

# Core Definition

Two graphs $G_1, G_2$ on vertex set $V$ are isomorphic iff there is a permutation $\pi$ of $V$ mapping edges of $G_1$ to edges of $G_2$. This is a special case of counting orbits: $X = V^{(2)}$ (pairs), $Y = \{0, 1\}$ (edge/non-edge), and $\Gamma$ is the permutation group on $X$ induced by $S_n$ on $V$. By Polya's theorem, the problem is solved when we know the cycle sum of $\Gamma_n$, though for large $n$ asymptotic formulae (from random graph techniques) are more practical (Bollobas, p. 291).

# Prerequisites

- **Polya's enumeration theorem** -- The counting tool
- **Group orbit** -- Isomorphism classes are orbits

# Key Properties

1. There are $2^{N}$ labelled graphs on $n$ vertices ($N = \binom{n}{2}$)
2. The number of unlabelled graphs is the number of $\Gamma_n^*$-orbits
3. For practical computation, asymptotic formulae from random graph theory are used
4. An extension covers self-complementary graphs ($S_2$ acting on $\{0,1\}$)

# Construction / Recognition

## Framework
1. Domain $D = V^{(2)}$ (vertex pairs)
2. Range $R = \{0, 1\}$ (edge indicator)
3. Group $\Gamma = $ permutations of $D$ induced by $S_n$ on $V$
4. Apply Polya's theorem with the cycle sum of $\Gamma$

# Context & Application

While Polya's theorem gives a theoretical solution, the cycle sum of $\Gamma_n$ is unwieldy for large $n$. In practice, the number of unlabelled graphs is approximately $2^N / n!$ for large $n$, since most graphs have trivial automorphism group.

# Examples

**Example** (p. 291): The explicit cycle sum for $\Gamma_n$ can be written down but is "not very inspiring" for practical calculations.

# Relationships

## Builds Upon
- **Polya's enumeration theorem** -- The tool
- **Group orbit** -- Isomorphism classes

## Enables
- Graph enumeration tables

## Related
- **Cayley's formula for trees** -- Labelled tree counting (easier)

## Contrasts With
- None

# Common Errors

- **Error**: Dividing $2^N$ by $n!$ to get the exact count
  **Correction**: The exact count requires Burnside/Polya; $2^N/n!$ is only an approximation (valid for large $n$ because most graphs have trivial automorphism group)

# Common Confusions

- **Confusion**: Confusing labelled and unlabelled graph counts
  **Clarification**: Labelled: $2^N$. Unlabelled: $\approx 2^N/n!$ for large $n$

# Source Reference

Chapter VIII, Section VIII.4, pages 284--285, 291.

# Verification Notes

- Definition source: Synthesized from pp. 284--285
- Confidence rationale: Clear discussion linking to Polya
- Uncertainties: None
- Cross-reference status: Verified
