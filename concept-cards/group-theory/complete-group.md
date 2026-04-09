---
# === CORE IDENTIFICATION ===
concept: Complete Group
slug: complete-group

# === CLASSIFICATION ===
category: automorphisms-extensions
subcategory: automorphisms
tier: intermediate

# === PROVENANCE ===
source: "Group Theory"
source_slug: group-theory
authors: "J.S. Milne"
chapter: "Automorphisms and Extensions"
chapter_number: 3
pdf_page: 43
section: "Complete groups"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - automorphism-group
  - inner-automorphism
  - centre-of-group
extends: []
related:
  - split-extension
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a complete group?"
---

# Quick Definition

A group $G$ is complete if the natural map $g \mapsto i_g : G \to \operatorname{Aut}(G)$ is an isomorphism.

# Core Definition

"A group $G$ is complete if the map $g \mapsto i_g : G \to \operatorname{Aut}(G)$ is an isomorphism" (Milne, Definition 3.3, p. 43). Equivalently, $G$ is complete if and only if (a) $Z(G) = 1$, and (b) every automorphism of $G$ is inner.

# Prerequisites

- **Automorphism group** — The codomain of the map $G \to \operatorname{Aut}(G)$
- **Inner automorphism** — Completeness requires all automorphisms are inner
- **Centre of group** — Completeness requires trivial centre

# Key Properties

1. $Z(G) = 1$ (trivial centre)
2. $\operatorname{Out}(G) = 1$ (every automorphism is inner)
3. If $N$ is complete and $N \trianglelefteq G$, then $G = N \times C_G(N)$ (Proposition 3.22)
4. If $G$ is simple and noncommutative, then $\operatorname{Aut}(G)$ is complete (Example 3.4b)

# Context & Application

Complete groups are "rigid" in that they have no external symmetries. An extension with a complete normal subgroup always splits as a direct product (Proposition 3.22).

# Examples

**Example 1** (p. 43): $S_n$ is complete for $n \neq 2, 6$. $S_2$ fails because $Z(S_2) \neq 1$; $S_6$ fails because it has outer automorphisms.

**Example 2** (p. 43): If $G$ is a simple noncommutative group, then $\operatorname{Aut}(G)$ is complete.

# Relationships

## Builds Upon
- **automorphism-group**, **inner-automorphism**, **centre-of-group**

## Enables
- **split-extension** — Extensions by complete normal subgroups split as direct products

# Common Errors

- **Error**: Assuming all symmetric groups are complete
  **Correction**: $S_2$ and $S_6$ are exceptions

# Source Reference

Chapter 3: Automorphisms and Extensions, "Complete groups", Definition 3.3, page 43.

# Verification Notes

- Definition source: Direct quote from Definition 3.3, p. 43
- Confidence: HIGH — explicit definition
- Uncertainties: None
