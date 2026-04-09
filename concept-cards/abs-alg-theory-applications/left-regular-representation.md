---
concept: Left Regular Representation
slug: left-regular-representation
category: morphisms
subcategory: null
tier: intermediate
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Isomorphisms"
chapter_number: 9
pdf_page: 131
section: "Cayley's Theorem"
extraction_confidence: high
aliases: []
prerequisites:
  - cayleys-theorem
extends: []
related:
  - permutation-group
contrasts_with: []
answers_questions:
  - "What is the left regular representation?"
---

# Quick Definition

The left regular representation of a group $G$ is the isomorphism $g \mapsto \lambda_g$ from Cayley's Theorem, where $\lambda_g : G \to G$ is defined by $\lambda_g(a) = ga$. It embeds $G$ into $S_G$.

# Core Definition

"The isomorphism $g \mapsto \lambda_g$ is known as the *left regular representation* of $G$" (Judson, p. 131). This is the specific isomorphism constructed in the proof of Cayley's Theorem.

# Prerequisites

- **Cayley's Theorem** — The left regular representation is the isomorphism from its proof

# Key Properties

1. $\lambda_g(a) = ga$ (left multiplication by $g$)
2. $\lambda_g$ is a permutation of $G$ for each $g$
3. $\lambda_{gh} = \lambda_g \circ \lambda_h$
4. $\lambda_e = \text{id}_G$
5. $\lambda_g^{-1} = \lambda_{g^{-1}}$

# Construction / Recognition

## To Construct:
1. For each $g \in G$, define $\lambda_g(a) = ga$
2. The map $\phi(g) = \lambda_g$ is the left regular representation

# Context & Application

The left regular representation provides a canonical way to realize any abstract group as a concrete permutation group. It is one of the most fundamental constructions in group theory.

# Examples

**Example 1** (p. 130): For $\mathbb{Z}_3$: $\lambda_0 = (0)$ (identity), $\lambda_1 = (012)$, $\lambda_2 = (021)$.

# Relationships

## Builds Upon
- **Cayley's Theorem** — This is the isomorphism from its proof

## Related
- **Permutation Group** — The image is a permutation group

# Common Errors

- **Error**: Defining $\lambda_g(a) = ag$ (right multiplication) instead of $ga$
  **Correction**: The *left* regular representation uses $\lambda_g(a) = ga$; the right version uses $\rho_g(a) = ag^{-1}$

# Common Confusions

- **Confusion**: Thinking the left regular representation is the only way to represent a group as permutations
  **Clarification**: It is the canonical way, but many other (possibly more efficient) representations exist

# Source Reference

Chapter 9: Isomorphisms, Section 9.1, page 131.

# Verification Notes

- Definition source: Direct from p. 131
- Confidence rationale: Explicit named concept
- Uncertainties: None
- Cross-reference status: Verified
