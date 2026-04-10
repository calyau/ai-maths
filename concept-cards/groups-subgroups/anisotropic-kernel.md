---
# === CORE IDENTIFICATION ===
concept: Anisotropic Kernel
slug: anisotropic-kernel

# === CLASSIFICATION ===
category: reductive-groups
subcategory: null
tier: advanced

# === PROVENANCE ===
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "The Structure of Reductive Groups: General Case"
chapter_number: 6
pdf_page: 395
section: "Relative root systems and the anisotropic kernel"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - reductive-algebraic-group
  - split-maximal-torus
  - root-system
extends: []
related:
  - relative-root-system
  - tits-index
  - form-of-algebraic-group
contrasts_with:
  - split-reductive-group

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What must I know before understanding arithmetic subgroups?"
---

# Quick Definition

The anisotropic kernel of a reductive group $G$ over $k$ is the derived group of the centralizer of a maximal split torus $T'$. It is a semisimple group over $k$ with no nontrivial split subtori, and it measures how far $G$ is from being split.

# Core Definition

For a reductive group $G$ over $k$, choose a torus $T'$ that is maximal among those that are split, and let $T$ be a maximal torus containing $T'$. "The derived group of the centralizer of $T'$ is called the *anisotropic kernel* of $G$ — it is a semisimple algebraic group over $k$ whose split subtori are trivial." (Milne, p. 395)

The isomorphism class of $G$ is determined by three data: the isomorphism class of $G_{k^{\mathrm{sep}}}$ (equivalently, the root datum), the anisotropic kernel, and the Tits index (Tits 1966).

# Prerequisites

- **Reductive algebraic group** — the anisotropic kernel is defined for reductive groups
- **Split maximal torus** — one starts by choosing a maximal split torus
- **Root system** — the relative root system is defined using the maximal split torus

# Key Properties

1. The anisotropic kernel is a semisimple algebraic group over $k$
2. It has no nontrivial split subtori (it is "anisotropic" in this sense)
3. The anisotropic kernel is trivial if and only if $G$ is split
4. It yields no information for anisotropic groups (those with no split torus at all)
5. Together with the index and the split type, it determines $G$ up to isomorphism

# Construction / Recognition

## To Construct:
1. Start with a reductive group $G$ over $k$
2. Choose a maximal split torus $T' \subset G$
3. Compute the centralizer $Z_G(T')$
4. The anisotropic kernel is the derived group $[Z_G(T'), Z_G(T')]$

## To Recognize:
1. A semisimple group is anisotropic (could be an anisotropic kernel) if it has no nontrivial split subtorus over $k$

# Context & Application

The anisotropic kernel is one of the three invariants in Tits's classification of semisimple groups over arbitrary fields. While split groups are classified by root data alone, non-split groups require the additional data of the anisotropic kernel and the index. The problem of classifying anisotropic kernels is related to the Brauer group of the field $k$.

# Examples

**Example 1** (p. 395): For a split group $G$, the maximal split torus is a maximal torus, its centralizer is the torus itself, and the anisotropic kernel is trivial.

**Example 2** (p. 395, from context): For $G = \mathrm{SL}_1(D)$ where $D$ is a division algebra of degree $n$ over $k$, $G$ has no split torus if $D$ is a division algebra, and the anisotropic kernel of an appropriate group is $G$ itself.

# Relationships

## Builds Upon
- **Reductive algebraic group** — the anisotropic kernel is defined within this theory
- **Split maximal torus** — the construction begins with a maximal split torus

## Enables
- **Tits index** — the index together with the anisotropic kernel classifies the group

## Related
- **Relative root system** — defined using the same maximal split torus
- **Form of algebraic group** — the anisotropic kernel is an invariant of the form

## Contrasts With
- **Split reductive group** — split groups have trivial anisotropic kernel

# Common Errors

- **Error**: Confusing "maximal split torus" with "maximal torus"
  **Correction**: The maximal split torus $T'$ may be much smaller than a maximal torus $T$; they coincide only when $G$ is split

# Common Confusions

- **Confusion**: Thinking the anisotropic kernel determines the group
  **Clarification**: The anisotropic kernel is only one of three invariants needed; the Tits index and the type over $k^{\mathrm{sep}}$ are also required

# Source Reference

Chapter VI: The Structure of Reductive Groups: General Case, Section 3, pages 395-396.

# Verification Notes

- Definition source: Direct quote from p. 395
- Confidence: HIGH — explicitly defined with clear terminology
- Uncertainties: Section 3 is a brief overview; full details reference Tits 1966 and Selbach 1976
- Cross-reference status: Verified
