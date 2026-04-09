---
# === CORE IDENTIFICATION ===
concept: Normal Subgroup
slug: normal-subgroup

# === CLASSIFICATION ===
category: subgroup-theory
subcategory: null
tier: foundational

# === PROVENANCE ===
source: "Group Theory"
source_slug: group-theory
authors: "J.S. Milne"
chapter: "Basic Definitions and Results"
chapter_number: 1
pdf_page: 18
section: "Normal subgroups"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - invariant subgroup

# === TYPED RELATIONSHIPS ===
prerequisites:
  - subgroup
  - left-coset
  - conjugation
extends:
  - subgroup
related:
  - kernel
  - quotient-group
  - simple-group
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a normal subgroup?"
  - "How do normal subgroups relate to quotient groups?"
  - "How does the kernel of a homomorphism relate to normal subgroups?"
---

# Quick Definition

A subgroup $N$ of $G$ is normal, denoted $N \trianglelefteq G$, if $gNg^{-1} = N$ for all $g \in G$. Normal subgroups are precisely the kernels of homomorphisms.

# Core Definition

"A subgroup $N$ of $G$ is *normal*, denoted $N \triangleleft G$, if $gNg^{-1} = N$ for all $g \in G$." (Milne, p. 18)

Equivalently (Proposition 1.34): $N$ is normal iff every left coset is also a right coset, i.e., $gN = Ng$ for all $g$.

# Prerequisites

- **Subgroup** — A normal subgroup is a subgroup with an additional property
- **Left coset** — Normality is characterized by coset equality
- **Conjugation** — Normality means invariance under conjugation

# Key Properties

1. $N \trianglelefteq G \iff gNg^{-1} = N$ for all $g \in G$
2. $N \trianglelefteq G \iff gN = Ng$ for all $g \in G$ (Proposition 1.34)
3. It suffices to check $gNg^{-1} \subset N$ for all $g$ (Remark 1.32)
4. Every subgroup of index 2 is normal (Example 1.36a)
5. Every subgroup of a commutative group is normal
6. Normal subgroups = kernels of homomorphisms (Propositions 1.41, 1.42)
7. If $H, N \le G$ and $N \trianglelefteq G$, then $HN$ is a subgroup (Proposition 1.37)
8. Intersections of normal subgroups are normal

# Construction / Recognition

## To Check Normality:
1. Show $gNg^{-1} \subset N$ for all $g \in G$, or
2. Show $N = \mathrm{Ker}(\alpha)$ for some homomorphism $\alpha$, or
3. Show $(G : N) = 2$

# Context & Application

Normal subgroups are essential for forming quotient groups. The relationship "normal subgroups = kernels" is foundational. Understanding when subgroups are normal is key to analyzing group structure.

# Examples

**Example 1** (p. 18): In $D_n$, the cyclic subgroup $C_n = \langle r \rangle$ has index 2, hence is normal.

**Example 2** (p. 18): For $n \ge 3$, the subgroup $\{e, s\}$ of $D_n$ is *not* normal: $r^{-1}sr = r^{n-2}s \notin \{e, s\}$.

**Example 3** (p. 19): Every subgroup of the quaternion group $Q$ is normal, even though $Q$ is noncommutative.

**Example 4** (p. 20): $\mathrm{SL}_n(F) = \mathrm{Ker}(\det) \trianglelefteq \mathrm{GL}_n(F)$.

# Relationships

## Builds Upon
- **subgroup** — a normal subgroup is a special type of subgroup
- **conjugation** — normality is invariance under conjugation

## Enables
- **quotient-group** — requires a normal subgroup
- **kernel** — the kernel is always normal
- **correspondence-theorem** — relates normal subgroups above and below a quotient

## Related
- **simple-group** — a group with no proper nontrivial normal subgroups

# Common Errors

- **Error**: Checking $gNg^{-1} \subset N$ for a *specific* $g$ and concluding normality
  **Correction**: Must check for *all* $g \in G$. Note: $gNg^{-1} \subsetneq N$ is possible for a specific $g$ in an infinite group (Example 1.33)

# Common Confusions

- **Confusion**: Thinking normality means elements of $N$ commute with all of $G$
  **Clarification**: Normality means $gn = n'g$ for *some* $n' \in N$, not $gn = ng$ (that would mean $N \subset Z(G)$)

# Source Reference

Chapter 1, Section "Normal subgroups", pages 18-20. Propositions 1.34, 1.37, 1.41, 1.42.

# Verification Notes

- Definition source: Direct quote from p. 18
- Confidence: HIGH — explicit definition
- Cross-reference status: Verified with multiple propositions
- Uncertainties: None
