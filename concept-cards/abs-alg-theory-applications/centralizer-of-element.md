---
# === CORE IDENTIFICATION ===
concept: Centralizer of an Element
slug: centralizer-of-element

# === CLASSIFICATION ===
category: group-structure
subcategory: subgroup-types
tier: intermediate

# === PROVENANCE ===
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Normal Subgroups and Factor Groups"
chapter_number: 10
pdf_page: 144
section: "Exercises"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "C(g)"
  - "centralizer subgroup"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - subgroup
  - group
extends:
  - subgroup
related:
  - center-of-group
  - conjugacy-class
  - class-equation
contrasts_with:
  - normalizer

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the centralizer of an element?"
  - "How does the centralizer relate to the center of a group?"
---

# Quick Definition

The centralizer of an element $g$ in a group $G$ is the set $C(g) = \{x \in G : xg = gx\}$ of all elements that commute with $g$. It is always a subgroup of $G$.

# Core Definition

"Define the centralizer of an element $g$ in a group $G$ to be the set $C(g) = \{x \in G : xg = gx\}$" (Judson, p. 144, Exercise 10.4.12). The centralizer $C(g)$ is a subgroup of $G$. If $g$ generates a normal subgroup of $G$, then $C(g)$ is normal in $G$.

# Prerequisites

- **Subgroup** — The centralizer is a subgroup
- **Group** — The ambient structure

# Key Properties

1. $C(g)$ is a subgroup of $G$ for every $g \in G$
2. $g \in C(g)$ always
3. $C(g) = G$ if and only if $g \in Z(G)$ (the center)
4. $Z(G) = \bigcap_{g \in G} C(g)$
5. The index $[G:C(g)]$ equals the size of the conjugacy class of $g$

# Construction / Recognition

## To Compute $C(g)$:
1. For each $x \in G$, check whether $xg = gx$
2. Collect all such $x$ into $C(g)$

# Context & Application

The centralizer appears prominently in the class equation: $|G| = |Z(G)| + [G:C(x_1)] + \cdots + [G:C(x_k)]$, where $x_1, \ldots, x_k$ represent the nontrivial conjugacy classes. The size of each conjugacy class is $[G:C(x_i)]$.

# Examples

**Example 1** (p. 184): In the class equation for $S_3$: the centralizer subgroups determine conjugacy class sizes. Since $6 = 1 + 2 + 3$, the centralizers have orders 6, 3, and 2 respectively.

# Relationships

## Builds Upon
- **Subgroup** — The centralizer is a subgroup

## Enables
- **Class equation** — Uses indices $[G:C(x_i)]$
- **Conjugacy class** — $|O_x| = [G:C(x)]$

## Related
- **Center of group** — $Z(G)$ is the intersection of all centralizers

## Contrasts With
- **Normalizer** — The normalizer of a subgroup $H$ is $N(H) = \{g : gHg^{-1} = H\}$; the centralizer is about individual elements

# Common Confusions

- **Confusion**: Confusing centralizer $C(g)$ with center $Z(G)$
  **Clarification**: $C(g)$ is relative to a specific element $g$; $Z(G)$ consists of elements that commute with ALL elements

# Source Reference

Chapter 10: Exercises 10.4.12-10.4.13, p. 144. Centralizer subgroups play a key role in the class equation (Chapter 14).

# Verification Notes

- Definition source: Direct from Exercise 10.4.12
- Confidence: HIGH — explicit definition
- Cross-reference status: Verified against Chapter 14 usage
