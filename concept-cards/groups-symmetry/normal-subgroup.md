---
# === CORE IDENTIFICATION ===
concept: Normal Subgroup
slug: normal-subgroup

# === CLASSIFICATION ===
category: normal-subgroups-quotients
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Groups and Symmetry"
source_slug: groups-symmetry
authors: "M.A. Armstrong"
chapter: "Quotient Groups"
chapter_number: 15
pdf_page: 86
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "invariant subgroup"
  - "$H \\triangleleft G$"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - subgroup
  - conjugacy-class
extends:
  - subgroup
related:
  - quotient-group
  - centre-of-a-group
  - commutator-subgroup
  - index-of-subgroup
contrasts_with:
  - subgroup

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a normal subgroup?"
  - "What distinguishes a normal subgroup from an ordinary subgroup?"
  - "How does the kernel of a homomorphism relate to normal subgroups?"
---

# Quick Definition

A subgroup $H$ of $G$ is normal (written $H \triangleleft G$) if it is a union of conjugacy classes of $G$. Equivalently, $gHg^{-1} \subseteq H$ for all $g \in G$, or equivalently $gH = Hg$ for all $g \in G$.

# Core Definition

A subgroup $H$ of a group $G$ is called a **normal subgroup** of $G$ if $H$ is a union of conjugacy classes of $G$ (Armstrong, Ch. 15, p. 86).

Normal subgroups are important because their left cosets form a group (the quotient group) under the natural multiplication $(xH)(yH) = xyH$.

# Prerequisites

- **Subgroup** — A normal subgroup is a subgroup with an additional property
- **Conjugacy class** — Normal subgroups are unions of conjugacy classes

# Key Properties

1. $H \triangleleft G$ iff $H$ is a union of conjugacy classes of $G$
2. Equivalently: $ghg^{-1} \in H$ for all $h \in H$, $g \in G$
3. Equivalently: $gH = Hg$ for all $g \in G$ (Theorem 15.3)
4. A subgroup of index 2 is always normal (Theorem 15.4)
5. The kernel of any homomorphism is normal (Theorem 16.1)
6. Every subgroup of an abelian group is normal (Example (iii))
7. To check normality, it suffices to check $xhx^{-1} \in H$ for generators $x$ of $G$ (Theorem 15.2)

# Construction / Recognition

## To Verify Normality:
1. **Method 1**: Check that $ghg^{-1} \in H$ for all $h \in H$ and $g \in G$
2. **Method 2**: Check that $gH = Hg$ for all $g \in G$
3. **Method 3** (Theorem 15.2): Check only for generators of $G$
4. **Method 4**: Check that $H$ is a union of complete conjugacy classes
5. **Shortcut**: If $[G:H] = 2$, then $H$ is automatically normal

# Context & Application

Armstrong devotes Chapter 15 to normal subgroups because they are precisely the subgroups for which the quotient construction works. The condition $gH = Hg$ ensures that the product of two cosets is again a coset: $(xH)(yH) = xyH$. Without normality, this product is not well-defined.

# Examples

**Example 1** (p. 87): $\langle r^3 \rangle = \{e, r^3\}$ is normal in $D_6$ as it is the union of classes $\{e\}$ and $\{r^3\}$.

**Example 2** (p. 87): $V = \{\varepsilon, (12)(34), (13)(24), (14)(23)\}$ is normal in $A_4$ (union of classes $\{\varepsilon\}$ and $\{(12)(34), (13)(24), (14)(23)\}$).

**Example 3** (p. 87): Every subgroup of an abelian group is normal.

**Example 4** (p. 88): $A_n \triangleleft S_n$ (index 2).

**Example 5** (p. 88): $\langle r \rangle \triangleleft D_n$ (index 2).

**Example 6** (p. 88): $SO_n \triangleleft O_n$ (index 2, also by determinant argument).

# Relationships

## Builds Upon
- **Subgroup** — A normal subgroup is a special type of subgroup
- **Conjugacy class** — Normality means being a union of conjugacy classes

## Enables
- **Quotient group** — Defined only for normal subgroups
- **Homomorphism** — Every kernel is normal; every normal subgroup is a kernel

## Related
- **Centre of a group** — Always normal
- **Commutator subgroup** — Always normal (Theorem 15.6)
- **Index of a subgroup** — Index 2 implies normality

## Contrasts With
- **Subgroup** (non-normal) — Not all subgroups are normal; $\langle (123) \rangle$ is not normal in $A_4$

# Common Errors

- **Error**: Thinking $gH = Hg$ means $gh = hg$ for all $h \in H$
  **Correction**: $gH = Hg$ is equality of *sets*, not element-wise commutativity. For each $h_1 \in H$ there exists $h_2 \in H$ with $gh_1 = h_2 g$, but $h_1 \neq h_2$ in general.

- **Error**: Checking normality against only some elements of $G$
  **Correction**: Must check all $g \in G$ (or use generators via Theorem 15.2)

# Common Confusions

- **Confusion**: Thinking every subgroup is normal
  **Clarification**: In non-abelian groups, most subgroups are not normal. For example, the subgroup $\langle s \rangle$ of $D_n$ is generally not normal.

- **Confusion**: Thinking normality is symmetric ($H \triangleleft G$ implies $G \triangleleft H$)
  **Clarification**: Normality is not symmetric. $H$ must be a subgroup of $G$ for $H \triangleleft G$ to make sense.

# Source Reference

Chapter 15: Quotient Groups, pp. 86-92 (pdf). Definition, Theorems (15.1)-(15.4).

# Verification Notes

- Definition source: Direct from p. 86
- Equivalent characterisations: Theorem (15.3) on p. 88
- Confidence rationale: HIGH — central definition with multiple characterisations
- Uncertainties: None
