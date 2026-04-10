---
# === CORE IDENTIFICATION ===
concept: Stabilizer of an Element
slug: stabilizer-of-element

# === CLASSIFICATION ===
category: graph-enumeration
subcategory: group-actions
tier: intermediate

# === PROVENANCE ===
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Graphs, Groups and Matrices"
chapter_number: 8
pdf_page: 285
section: "VIII.4 Enumeration and Pólya's Theorem"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - isotropy group
  - point stabilizer

# === TYPED RELATIONSHIPS ===
prerequisites:
  - group-orbit
extends: []
related:
  - cauchy-frobenius-lemma
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the stabilizer of an element under a group action?"
---

# Quick Definition

The stabilizer of $x$ under $\Gamma$ is $\Gamma(x) = \{\alpha \in \Gamma : \alpha x = x\}$, the subgroup of elements fixing $x$. The orbit-stabilizer relation gives $|\Gamma| = |[x]| \cdot |\Gamma(x)|$.

# Core Definition

For a group $\Gamma$ acting on $X$ and $x \in X$: $\Gamma(x) = \Gamma(x, x) = \{\alpha \in \Gamma : \alpha x = x\}$ is the stabilizer of $x$; it is a subgroup of $\Gamma$. More generally, $\Gamma(x, y) = \{\alpha : \alpha x = y\}$ is a coset of $\Gamma(x)$. The key relation: $|\Gamma| = |[x]| \cdot |\Gamma(x)|$. The stabilizer size depends only on the orbit: $s([x]) = |\Gamma(x)|$ (Bollobas, p. 285).

# Prerequisites

- **Group orbit** -- Orbits and stabilizers are dual concepts

# Key Properties

1. $\Gamma(x)$ is a subgroup of $\Gamma$
2. $|\Gamma(x)|$ is constant on orbits
3. $\Gamma(x, y) = \beta\Gamma(x)$ for any $\beta$ with $\beta x = y$
4. $x \in F(\alpha)$ iff $\alpha \in \Gamma(x)$

# Construction / Recognition

Not applicable -- this is a definitional concept.

# Context & Application

Stabilizers appear in the proof of the Cauchy-Frobenius lemma and are essential for understanding how symmetry reduces counting problems.

# Examples

**Example** (p. 286): For $\Gamma = \{1, (12), (34), (12)(34)\}$ on $\{1,2,3,4\}$: $\Gamma(1) = \{1, (34)\}$, $|\Gamma(1)| = 2$, $|[1]| = 2$, $|\Gamma| = 4 = 2 \cdot 2$.

# Relationships

## Builds Upon
- **Group orbit** -- Dual concept

## Enables
- **Cauchy-Frobenius lemma** -- Uses the orbit-stabilizer relation

## Related
- **Cauchy-Frobenius lemma** -- Key ingredient

## Contrasts With
- None

# Common Errors

- **Error**: Confusing $\Gamma(x)$ with $F(\alpha)$
  **Correction**: $\Gamma(x)$ is the set of permutations fixing $x$; $F(\alpha)$ is the set of elements fixed by $\alpha$

# Common Confusions

- **Confusion**: Thinking the stabilizer of all elements is trivial
  **Clarification**: The kernel of the action (intersection of all stabilizers) is trivial for faithful actions, but individual stabilizers can be large

# Source Reference

Chapter VIII, Section VIII.4, page 285.

# Verification Notes

- Definition source: Direct from p. 285
- Confidence rationale: Explicit definition
- Uncertainties: None
- Cross-reference status: Verified
