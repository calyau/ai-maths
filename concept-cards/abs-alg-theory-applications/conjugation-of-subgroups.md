---
# === CORE IDENTIFICATION ===
concept: Conjugation of Subgroups
slug: conjugation-of-subgroups

# === CLASSIFICATION ===
category: group-structure
subcategory: subgroup-relations
tier: intermediate

# === PROVENANCE ===
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Normal Subgroups and Factor Groups"
chapter_number: 10
pdf_page: 138
section: "Factor Groups and Normal Subgroups"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "conjugate subgroup"
  - "gHg^{-1}"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - subgroup
  - conjugation-of-elements
extends: []
related:
  - normal-subgroup
  - normalizer
  - conjugacy-class
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What does it mean to conjugate a subgroup?"
  - "How does conjugation of subgroups relate to normality?"
---

# Quick Definition

For a subgroup $H$ of $G$ and an element $g \in G$, the conjugate subgroup $gHg^{-1} = \{ghg^{-1} : h \in H\}$ is always a subgroup of $G$. A subgroup is normal precisely when it equals all of its conjugates.

# Core Definition

Given a group $G$, a subgroup $H$, and an element $g \in G$, the set $gHg^{-1} = \{ghg^{-1} : h \in H\}$ is called a **conjugate** of $H$ by $g$. By Theorem 10.3 (p. 138), $H$ is normal in $G$ if and only if $gHg^{-1} = H$ for all $g \in G$, which is equivalent to $gHg^{-1} \subset H$ for all $g \in G$.

# Prerequisites

- **Subgroup** — Conjugation acts on subgroups
- **Conjugation of elements** — The operation $g \cdot h = ghg^{-1}$ applied set-wise

# Key Properties

1. $gHg^{-1}$ is always a subgroup of $G$ (isomorphic to $H$)
2. $|gHg^{-1}| = |H|$ for all $g \in G$
3. $eHe^{-1} = H$
4. $(g_1g_2)H(g_1g_2)^{-1} = g_1(g_2Hg_2^{-1})g_1^{-1}$
5. $H$ is normal if and only if $gHg^{-1} = H$ for all $g \in G$
6. $gHg^{-1} \subset H$ for all $g$ implies $gHg^{-1} = H$ for all $g$

# Construction / Recognition

## To Compute a Conjugate Subgroup:
1. Take each element $h \in H$
2. Compute $ghg^{-1}$ for the given $g$
3. Collect all results: $gHg^{-1} = \{ghg^{-1} : h \in H\}$

# Context & Application

Conjugation of subgroups is the key mechanism for understanding normal subgroups. It also underlies the Sylow theorems, where the number of Sylow $p$-subgroups equals the number of conjugates of any one Sylow $p$-subgroup.

# Examples

**Example 1** (p. 138): In $S_3$, conjugating $H = \{(1), (12)\}$ by $(123)$ gives $(123)H(132) = \{(1), (23)\} \neq H$, showing $H$ is not normal.

**Example 2** (p. 140): In $D_n$, $sR_ns^{-1} = R_n$ since $srs = r^{-1} \in R_n$, confirming $R_n$ is normal.

# Relationships

## Builds Upon
- **Subgroup** — Conjugation acts on subgroups

## Enables
- **Normal subgroup** — Characterized by $gHg^{-1} = H$
- **Normalizer** — $N(H) = \{g \in G : gHg^{-1} = H\}$

## Related
- **Conjugacy class** — Conjugacy classes of subgroups partition the set of subgroups of a given order

# Common Errors

- **Error**: Assuming $gHg^{-1} \subset H$ is strictly weaker than $gHg^{-1} = H$
  **Correction**: By Theorem 10.3, $gHg^{-1} \subset H$ for all $g$ implies $gHg^{-1} = H$ for all $g$

# Common Confusions

- **Confusion**: Confusing conjugation of elements ($ghg^{-1}$) with conjugation of subgroups ($gHg^{-1}$)
  **Clarification**: Conjugation of subgroups applies conjugation to every element of the subgroup simultaneously

# Source Reference

Chapter 10: Normal Subgroups and Factor Groups, Section 10.1, pages 138-139. Theorem 10.3 establishes the equivalence of normality conditions.

# Verification Notes

- Definition source: Synthesized from Theorem 10.3 discussion
- Confidence: HIGH — directly stated in theorem
- Cross-reference status: Verified
