---
concept: Cayley's Theorem
slug: cayleys-theorem
category: morphisms
subcategory: null
tier: intermediate
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Isomorphisms"
chapter_number: 9
pdf_page: 130
section: "Cayley's Theorem"
extraction_confidence: high
aliases: []
prerequisites:
  - group-isomorphism
  - permutation-group
extends: []
related:
  - left-regular-representation
  - symmetric-group
contrasts_with: []
answers_questions:
  - "What is Cayley's theorem?"
  - "How does Cayley's theorem connect abstract groups to permutation groups?"
---

# Quick Definition

Cayley's Theorem states that every group is isomorphic to a group of permutations. The isomorphism sends each element $g$ to the left multiplication map $\lambda_g(a) = ga$.

# Core Definition

**Theorem 9.12 (Cayley):** "Every group is isomorphic to a group of permutations" (Judson, p. 130). The proof constructs, for each $g \in G$, the permutation $\lambda_g : G \to G$ defined by $\lambda_g(a) = ga$. The map $\phi : G \to \overline{G}$ given by $\phi(g) = \lambda_g$ is an isomorphism from $G$ to the group $\overline{G} = \{\lambda_g : g \in G\}$ of permutations.

# Prerequisites

- **Group Isomorphism** — Cayley's theorem provides an isomorphism
- **Permutation Group** — Every group is isomorphic to a permutation group

# Key Properties

1. Every group embeds into a symmetric group
2. A group of order $n$ embeds into $S_n$
3. The construction uses left multiplication: $\lambda_g(a) = ga$
4. $\lambda_g \circ \lambda_h = \lambda_{gh}$ (composition corresponds to group multiplication)
5. The map $g \mapsto \lambda_g$ is called the left regular representation

# Construction / Recognition

## To Construct the Embedding:
1. For each $g \in G$, define $\lambda_g : G \to G$ by $\lambda_g(a) = ga$
2. Show $\lambda_g$ is a bijection (hence a permutation) of $G$
3. The set $\overline{G} = \{\lambda_g : g \in G\}$ forms a permutation group
4. The map $g \mapsto \lambda_g$ is the desired isomorphism

# Context & Application

Cayley's Theorem is a representation theorem. It shows that permutation groups are not just special examples -- they are the universal model for all groups. This connects abstract group theory to the concrete world of permutations.

# Examples

**Example 1** (p. 130): $\mathbb{Z}_3 \cong \{(0), (012), (021)\}$. The isomorphism sends $0 \mapsto (0)$ (identity), $1 \mapsto (012)$, $2 \mapsto (021)$.

# Relationships

## Builds Upon
- **Group Isomorphism** — The theorem provides an isomorphism
- **Permutation Group** — The target of the isomorphism

## Enables
- **Left Regular Representation** — The specific isomorphism constructed

## Related
- **Symmetric Group** — Every group embeds into some $S_n$

# Common Errors

- **Error**: Thinking Cayley's Theorem means every group *is* a permutation group
  **Correction**: It means every group is *isomorphic to* a permutation group; the original group may be defined abstractly

# Common Confusions

- **Confusion**: Thinking the embedding into $S_n$ is the most efficient
  **Clarification**: Cayley's Theorem embeds $G$ into $S_{|G|}$, which is usually much larger than necessary. More efficient embeddings may exist.

# Source Reference

Chapter 9: Isomorphisms, Section 9.1, "Cayley's Theorem," Theorem 9.12, pages 130-131.

# Verification Notes

- Definition source: Direct from Theorem 9.12
- Confidence rationale: Explicit named theorem with proof
- Uncertainties: None
- Cross-reference status: Verified
