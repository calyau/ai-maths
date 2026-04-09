---
# === CORE IDENTIFICATION ===
concept: Normal Subgroup
slug: normal-subgroup

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
pdf_page: 138
section: "Factor Groups and Normal Subgroups"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "invariant subgroup"
  - "self-conjugate subgroup"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - subgroup
  - coset
  - conjugation-of-elements
extends:
  - subgroup
related:
  - factor-group
  - kernel-of-homomorphism
  - conjugation-of-subgroups
contrasts_with:
  - subgroup

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a normal subgroup?"
  - "What distinguishes a normal subgroup from an arbitrary subgroup?"
  - "How do I determine if a subgroup is normal?"
  - "How do normal subgroups relate to factor groups?"
---

# Quick Definition

A subgroup $H$ of a group $G$ is normal in $G$ if the left and right cosets coincide, that is, $gH = Hg$ for all $g \in G$. Normal subgroups are precisely the subgroups that allow the construction of factor (quotient) groups.

# Core Definition

A subgroup $H$ of a group $G$ is **normal** in $G$ if $gH = Hg$ for all $g \in G$. "That is, a normal subgroup of a group $G$ is one in which the right and left cosets are precisely the same" (Judson, p. 138). Equivalently, $H$ is normal if and only if $gHg^{-1} \subset H$ for all $g \in G$, which is further equivalent to $gHg^{-1} = H$ for all $g \in G$ (Theorem 10.3).

# Prerequisites

- **Subgroup** — A normal subgroup is a special type of subgroup
- **Coset** — Normality is defined in terms of left and right cosets coinciding
- **Conjugation** — The equivalent characterization uses conjugation: $gHg^{-1} = H$

# Key Properties

1. Every subgroup of an abelian group is normal
2. $H$ is normal in $G$ if and only if $gHg^{-1} \subset H$ for all $g \in G$
3. $H$ is normal in $G$ if and only if $gHg^{-1} = H$ for all $g \in G$
4. The trivial subgroup $\{e\}$ and $G$ itself are always normal in $G$
5. Any subgroup of index 2 is normal
6. The kernel of any group homomorphism is a normal subgroup
7. The intersection of two normal subgroups is normal

# Construction / Recognition

## To Determine if a Subgroup is Normal:
1. Check if $gHg^{-1} \subset H$ for all $g \in G$
2. Alternatively, verify that every left coset equals the corresponding right coset
3. If $H$ has index 2 in $G$, then $H$ is automatically normal
4. If $H$ is the kernel of some homomorphism, then $H$ is normal

## To Find Normal Subgroups:
1. In an abelian group, every subgroup is normal
2. Look for subgroups of index 2
3. Compute kernels of known homomorphisms
4. Check the center $Z(G)$, which is always normal

# Context & Application

Normal subgroups play a critical role in group theory because they are precisely the subgroups that allow the construction of factor (quotient) groups. They are also exactly the kernels of group homomorphisms. The concept is central to the classification of groups and to understanding group structure through the isomorphism theorems.

# Examples

**Example 1** (p. 138): Every subgroup of an abelian group is normal, since $gh = hg$ for all $g \in G$ and $h \in H$ implies $gH = Hg$.

**Example 2** (p. 138): In $S_3$, the subgroup $H = \{(1), (12)\}$ is **not** normal since $(123)H = \{(123), (13)\} \neq H(123) = \{(123), (23)\}$. However, the subgroup $N = \{(1), (123), (132)\}$ is normal since $N = (12)N = N(12)$.

**Example 3** (p. 140): In the dihedral group $D_n$, the rotation subgroup $R_n = \langle r \rangle$ is normal since $srs^{-1} = r^{-1} \in R_n$.

# Relationships

## Builds Upon
- **Subgroup** — A normal subgroup is a subgroup with an additional symmetry property
- **Coset** — Normality means left and right cosets are equal

## Enables
- **Factor group** — Can only be constructed from normal subgroups
- **Isomorphism theorems** — All depend on normal subgroups
- **Simple group** — Defined in terms of absence of nontrivial normal subgroups

## Related
- **Kernel of homomorphism** — Every kernel is a normal subgroup, and every normal subgroup is a kernel
- **Conjugation of subgroups** — $gHg^{-1} = H$ characterizes normality

## Contrasts With
- **Subgroup** — An arbitrary subgroup need not have $gH = Hg$

# Common Errors

- **Error**: Assuming $gH = Hg$ means $gh = hg$ for all $h \in H$
  **Correction**: $gH = Hg$ means for each $h \in H$ there exists $h' \in H$ such that $gh = h'g$, not that $g$ commutes with every element of $H$

- **Error**: Checking normality by testing only a few elements $g \in G$
  **Correction**: The condition $gHg^{-1} \subset H$ must hold for ALL $g \in G$

# Common Confusions

- **Confusion**: Believing that normality is a property of the subgroup alone
  **Clarification**: Normality depends on the ambient group. A subgroup can be normal in one group but not in a larger group

- **Confusion**: Thinking every subgroup is normal
  **Clarification**: Only in abelian groups is every subgroup normal. In non-abelian groups, many subgroups fail to be normal

# Source Reference

Chapter 10: Normal Subgroups and Factor Groups, Section 10.1, pages 138-140. See Theorem 10.3 for equivalent characterizations.

# Verification Notes

- Definition source: Direct quote from p. 138
- Key properties: Theorem 10.3 (p. 138) provides equivalent characterizations
- Examples: All from source text
- Confidence: HIGH — explicit definition with theorem and multiple examples
- Cross-reference status: All slugs verified against planned extractions
