---
# === CORE IDENTIFICATION ===
concept: Characteristic Subgroup
slug: characteristic-subgroup

# === CLASSIFICATION ===
category: automorphisms-extensions
subcategory: subgroup-properties
tier: intermediate

# === PROVENANCE ===
source: "Group Theory"
source_slug: group-theory
authors: "J.S. Milne"
chapter: "Automorphisms and Extensions"
chapter_number: 3
pdf_page: 44
section: "Characteristic subgroups"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - normal-subgroup
  - automorphism
extends:
  - normal-subgroup
related:
  - centre-of-group
contrasts_with:
  - normal-subgroup

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What distinguishes a normal subgroup from a characteristic subgroup?"
---

# Quick Definition

A characteristic subgroup of $G$ is a subgroup $H$ that is invariant under every automorphism of $G$: $\alpha(H) = H$ for all $\alpha \in \operatorname{Aut}(G)$.

# Core Definition

"A characteristic subgroup of a group $G$ is a subgroup $H$ such that $\alpha(H) = H$ for all automorphisms $\alpha$ of $G$" (Milne, Definition 3.6, p. 44).

# Prerequisites

- **Normal subgroup** — Characteristic implies normal; a subgroup is normal if stable under all inner automorphisms
- **Automorphism** — Characteristic means stable under all automorphisms, not just inner ones

# Key Properties

1. Characteristic $\implies$ normal (since inner automorphisms are automorphisms)
2. Normal $\centernot\implies$ characteristic (Remark 3.7d)
3. It suffices to check $\alpha(H) \subset H$ for all $\alpha \in \operatorname{Aut}(G)$
4. A characteristic subgroup of a characteristic subgroup is characteristic in the ambient group
5. A characteristic subgroup of a normal subgroup is normal in the ambient group (Remark 3.7a)
6. The centre $Z(G)$ is always characteristic (Remark 3.7b)
7. If $H$ is the unique subgroup of $G$ of a given order, then $H$ is characteristic (Remark 3.7c)

# Construction / Recognition

## To verify $H$ is characteristic in $G$:
1. Show $\alpha(H) \subset H$ for all $\alpha \in \operatorname{Aut}(G)$
2. Alternatively, show $H$ is defined by a group-theoretic property (e.g., $Z(G)$, commutator subgroup)
3. Or show $H$ is the unique subgroup of its order in $G$

# Context & Application

Characteristic subgroups are "more invariant" than normal subgroups. They arise naturally from group-theoretic constructions. The distinction matters when analyzing chains of subgroups: a normal subgroup of a normal subgroup need not be normal, but a characteristic subgroup of a characteristic subgroup is always characteristic.

# Examples

**Example 1** (p. 45): The centre $Z(G)$ is characteristic in $G$.

**Example 2** (p. 45): Every subspace of dimension 1 in $\mathbb{F}_p^2$ is a (normal) subgroup but not characteristic, since $\operatorname{Aut}(\mathbb{F}_p^2) = \operatorname{GL}_2(\mathbb{F}_p)$ moves lines.

# Relationships

## Builds Upon
- **normal-subgroup** — Characteristic implies normal

## Contrasts With
- **normal-subgroup** — Normal means stable under inner automorphisms only; characteristic means stable under all automorphisms

# Common Errors

- **Error**: Assuming a normal subgroup of a normal subgroup is normal in the ambient group
  **Correction**: This can fail. However, a characteristic subgroup of a normal subgroup is always normal in the ambient group (Remark 3.7a)

# Common Confusions

- **Confusion**: Thinking characteristic and normal are the same
  **Clarification**: In a commutative group, every subgroup is normal but not every subgroup is characteristic (Remark 3.7d)

# Source Reference

Chapter 3: Automorphisms and Extensions, "Characteristic subgroups", Definition 3.6, page 44.

# Verification Notes

- Definition source: Direct quote from Definition 3.6, p. 44
- Confidence: HIGH — explicit definition
- Uncertainties: None
