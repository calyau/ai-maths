---
# === CORE IDENTIFICATION ===
concept: Group Orbit
slug: group-orbit

# === CLASSIFICATION ===
category: graph-enumeration
subcategory: group-actions
tier: foundational

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
  - orbit of a group action

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - stabilizer-of-element
  - cauchy-frobenius-lemma
  - pattern-enumeration
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an orbit of a group action?"
---

# Quick Definition

The orbit of $x$ under a group $\Gamma$ acting on set $X$ is $[x] = \{y \in X : y = \alpha x \text{ for some } \alpha \in \Gamma\}$, the set of all elements equivalent to $x$.

# Core Definition

Let $\Gamma$ be a group of permutations acting on a set $X$. For $x, y \in X$, put $x \sim y$ if $y = \alpha x$ for some $\alpha \in \Gamma$. The equivalence class $[x]$ is the $\Gamma$-orbit of $x$. The orbit-stabilizer relation gives $|\Gamma| = |[x]| \cdot |\Gamma(x)|$ where $\Gamma(x) = \{\alpha : \alpha x = x\}$ is the stabilizer (Bollobas, p. 285).

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. Orbits partition $X$
2. $|\Gamma| = |[x]| \cdot |\Gamma(x)|$ (orbit-stabilizer theorem)
3. $\Gamma(x, y) = \beta\Gamma(x)$ where $y = \beta x$ (stabilizer coset)
4. Two configurations have the same pattern iff they are in the same orbit

# Construction / Recognition

## To Find Orbits
1. Pick any $x \in X$
2. Compute $[x] = \{\alpha x : \alpha \in \Gamma\}$
3. Remove $[x]$ from $X$ and repeat

# Context & Application

Orbits are the fundamental objects in Polya enumeration. Counting graphs up to isomorphism is counting orbits of $\{0,1\}^{V^{(2)}}$ under the permutation group induced by $S_n$ on vertex pairs.

# Examples

**Example** (p. 286): $X = \{1,2,3,4\}$, $\Gamma = \{1, (12), (34), (12)(34)\}$: orbits are $\{1,2\}$ and $\{3,4\}$.

# Relationships

## Builds Upon
- No prerequisites

## Enables
- **Cauchy-Frobenius lemma** -- Counts orbits
- **Pattern enumeration** -- Patterns are orbits in a function space
- **Polya's enumeration theorem** -- Counts weighted orbits

## Related
- **Stabilizer of an element** -- Dual concept via orbit-stabilizer theorem

## Contrasts With
- None

# Common Errors

- **Error**: Confusing the orbit with the stabilizer
  **Correction**: The orbit is a subset of $X$; the stabilizer is a subgroup of $\Gamma$

# Common Confusions

- **Confusion**: Thinking all orbits have the same size
  **Clarification**: Orbits can have different sizes; the orbit-stabilizer theorem relates orbit size to stabilizer order

# Source Reference

Chapter VIII, Section VIII.4, pages 285--286.

# Verification Notes

- Definition source: Direct from p. 285
- Confidence rationale: Explicit definition
- Uncertainties: None
- Cross-reference status: Verified
