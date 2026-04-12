---
# === CORE IDENTIFICATION ===
concept: Quotient Group
slug: quotient-group

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
  - "factor group"
  - "$G/H$"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - normal-subgroup
  - left-coset
extends: []
related:
  - homomorphism
  - first-isomorphism-theorem
  - commutator-subgroup
  - index-of-subgroup
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a quotient group?"
  - "How do you form a group from cosets?"
---

# Quick Definition

If $H$ is a normal subgroup of $G$, the quotient group $G/H$ is the group of left cosets of $H$ in $G$, with multiplication $(xH)(yH) = xyH$. It has order $|G|/|H|$.

# Core Definition

**(15.1) Theorem.** If $H$ is a normal subgroup of $G$, the set of all left cosets of $H$ in $G$ forms a group under the multiplication $(xH)(yH) = xyH$ (Armstrong, Ch. 15, p. 86).

The coset $eH = H$ is the identity, $x^{-1}H$ is the inverse of $xH$, and associativity follows from associativity in $G$.

The key role of normality: for the formula $(xH)(yH) = xyH$ to hold, one needs $xhyh' = xy(y^{-1}hy)h'$, and the conjugate $y^{-1}hy$ belongs to $H$ precisely because $H$ is normal. The group $G/H$ is called the **quotient group** (or factor group) of $G$ by $H$, written $G/H$.

# Prerequisites

- **Normal subgroup** — The quotient is only defined when $H \triangleleft G$
- **Left coset** — Elements of $G/H$ are the left cosets of $H$

# Key Properties

1. $|G/H| = [G:H] = |G|/|H|$ (for finite groups)
2. The identity element is $eH = H$
3. The inverse of $xH$ is $x^{-1}H$
4. $(xH)(yH) = xyH$ (well-defined only because $H$ is normal)
5. The natural map $\varphi: G \to G/H$ defined by $\varphi(x) = xH$ is a surjective homomorphism with kernel $H$

# Construction / Recognition

## To Construct $G/H$:
1. Verify $H \triangleleft G$
2. List the distinct left cosets of $H$ in $G$
3. Define multiplication: $(xH)(yH) = xyH$
4. Identify the resulting group structure

# Context & Application

The quotient construction is one of the central ideas in group theory. It "divides out" the normal subgroup, producing a simpler group that captures the structure of $G$ modulo $H$. Armstrong notes: "Each of these cosets represents a *single element* in $G/H$ and it is in this sense that we have 'divided $G$ by $H$'" (p. 87).

# Examples

**Example 1** (p. 87): $D_6 / \langle r^3 \rangle$ has six cosets and is isomorphic to $D_3$. The cosets behave like elements of $D_3$: $(rH)^3 = r^3 H = H$, $(sH)^2 = H$, $(sH)(rH) = (rH)^2(sH)$.

**Example 2** (p. 87): $A_4 / V \cong \mathbb{Z}_3$ where $V = \{\varepsilon, (12)(34), (13)(24), (14)(23)\}$. Three cosets: $\varepsilon V$, $(123)V$, $(132)V$.

**Example 3** (p. 88): $\mathbb{Z}/n\mathbb{Z} \cong \mathbb{Z}_n$, with cosets $0 + n\mathbb{Z}, 1 + n\mathbb{Z}, \ldots, (n-1) + n\mathbb{Z}$.

# Relationships

## Builds Upon
- **Normal subgroup** — Required for the construction
- **Left coset** — Elements of the quotient group

## Enables
- **First isomorphism theorem** — $G/\ker(\varphi) \cong \operatorname{im}(\varphi)$
- **Abelianisation** — $G/[G,G]$ is the largest abelian quotient

## Related
- **Homomorphism** — The natural map $G \to G/H$ is a homomorphism
- **Index of a subgroup** — $|G/H| = [G:H]$

# Common Errors

- **Error**: Trying to form $G/H$ when $H$ is not normal
  **Correction**: The multiplication $(xH)(yH) = xyH$ is well-defined only when $H$ is normal

- **Error**: Confusing elements of $G/H$ (which are cosets, i.e., sets) with elements of $G$
  **Correction**: Each element of $G/H$ is a coset containing $|H|$ elements of $G$

# Common Confusions

- **Confusion**: Thinking $G/H$ is a subgroup of $G$
  **Clarification**: $G/H$ is a new group whose elements are cosets. It is not a subgroup of $G$ but a quotient of $G$.

- **Confusion**: Thinking quotient groups are always smaller
  **Clarification**: For finite groups, $|G/H| = |G|/|H| < |G|$ (unless $H = \{e\}$). For infinite groups, the quotient can have any size.

# Source Reference

Chapter 15: Quotient Groups, Theorem (15.1), pp. 86-88 (pdf). Examples (i)-(iv).

# Verification Notes

- Definition source: Direct from Theorem (15.1), p. 86
- Proof: Complete, showing why normality is needed
- Confidence rationale: HIGH — central definition with detailed proof
- Uncertainties: None
