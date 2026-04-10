---
# === CORE IDENTIFICATION ===
concept: Cauchy-Frobenius Lemma
slug: cauchy-frobenius-lemma

# === CLASSIFICATION ===
category: graph-enumeration
subcategory: orbit-counting
tier: intermediate

# === PROVENANCE ===
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Graphs, Groups and Matrices"
chapter_number: 8
pdf_page: 286
section: "VIII.4 Enumeration and Pólya's Theorem"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - Burnside's lemma
  - orbit-counting theorem

# === TYPED RELATIONSHIPS ===
prerequisites:
  - group-orbit
  - stabilizer-of-element
extends: []
related:
  - polya-enumeration-theorem
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I count the number of orbits of a group action?"
  - "What must I know before understanding Pólya's enumeration theorem?"
---

# Quick Definition

The number of orbits of a group $\Gamma$ acting on a set $X$ is $N(\Gamma) = \frac{1}{|\Gamma|}\sum_{\alpha \in \Gamma} |F(\alpha)|$, the average number of fixed points.

# Core Definition

**Lemma 22** (Bollobas, p. 286): Let $\Gamma$ act on $X$ with orbits $O_1, \ldots, O_\ell$ and weight function $w: X \to A$ constant on orbits. Then $|\Gamma|\sum_{i=1}^\ell w(O_i) = \sum_{\alpha \in \Gamma} \sum_{x \in F(\alpha)} w(x)$, where $F(\alpha) = \{x : \alpha x = x\}$. Taking $w \equiv 1$: $N(\Gamma) = \frac{1}{|\Gamma|}\sum_\alpha |F(\alpha)|$.

# Prerequisites

- **Group orbit** -- The objects being counted
- **Stabilizer of an element** -- $\Gamma(x) = \{\alpha : \alpha x = x\}$, used in the proof

# Key Properties

1. The number of orbits = average number of fixed points
2. Generalizes to weighted version for any abelian group $A$
3. Foundation for Polya's theorem (which is the function-space version)
4. Proof uses $|\Gamma| = |[x]| \cdot |\Gamma(x)|$

# Construction / Recognition

## To Count Orbits
1. List all elements $\alpha$ of $\Gamma$
2. For each $\alpha$, count $|F(\alpha)|$ (fixed points)
3. Sum and divide by $|\Gamma|$

# Context & Application

The lemma (historically attributed to Burnside, though due to Cauchy and Frobenius) is the unweighted precursor to Polya's theorem. It directly solves many counting-under-symmetry problems.

# Examples

**Example 1** (p. 286): $X = \{1,2,3,4\}$, $\Gamma = \{1, (12), (34), (12)(34)\}$: $N = \frac{1}{4}(4+2+2+0) = 2$.

**Example 2** (p. 286): Bracelets of 5 beads, 3 colors, cyclic symmetry: $N = \frac{1}{5}(243 + 3 + 3 + 3 + 3) = 51$.

**Example 3** (p. 287): Coloring faces of a cube with 3 colors: $N = \frac{1}{24}(3^6 + 8\cdot3^2 + 6\cdot3^3 + 3\cdot3^4 + 6\cdot3^3) = 57$.

# Relationships

## Builds Upon
- **Group orbit** -- The objects being counted
- **Stabilizer of an element** -- Key to the proof

## Enables
- **Polya's enumeration theorem** -- Weighted generalization to function spaces

## Related
- **Polya's enumeration theorem** -- The full generalization

## Contrasts With
- None

# Common Errors

- **Error**: Counting only non-identity elements of $\Gamma$
  **Correction**: Include the identity, which fixes all elements of $X$

# Common Confusions

- **Confusion**: Attributing the lemma to Burnside
  **Clarification**: Though commonly called "Burnside's lemma," the result is due to Cauchy and Frobenius; Burnside used it extensively

# Source Reference

Chapter VIII, Section VIII.4, Lemma 22, pages 286--287.

# Verification Notes

- Definition source: Direct from Lemma 22, p. 286
- Confidence rationale: Explicit lemma with proof and examples
- Uncertainties: None
- Cross-reference status: Verified
