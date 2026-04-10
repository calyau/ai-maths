---
# === CORE IDENTIFICATION ===
concept: Tits Index
slug: tits-index

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
extraction_confidence: medium

# === VARIANTS (authority control) ===
aliases:
  - Tits diagram
  - index of an algebraic group

# === TYPED RELATIONSHIPS ===
prerequisites:
  - relative-root-system
  - anisotropic-kernel
  - reductive-algebraic-group
extends: []
related:
  - inner-form
  - form-of-algebraic-group
  - galois-cohomology-of-algebraic-groups
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does Galois cohomology classify forms of algebraic groups?"
---

# Quick Definition

The Tits index of a semisimple group $G$ over $k$ is the triple $(S, S_0, \text{Galois action})$ where $S$ is a simple system of absolute roots, $S_0 \subset S$ is the subset vanishing on the maximal split torus, and the Galois group of $k^{\mathrm{sep}}/k$ acts on $S$. Together with the anisotropic kernel, it determines $G$ up to isomorphism.

# Core Definition

Let $G$ be a semisimple algebraic group over $k$, $T'$ a maximal split subtorus, $T \supset T'$ a maximal torus, and $S$ a simple set of roots for $(G_{k^{\mathrm{sep}}}, T_{k^{\mathrm{sep}}})$. Let $S_0$ be the subset of $S$ vanishing on $T'$. "The Galois group of $K/k$ acts on $S$, and the triple consisting of $S$, $S_0$, and this action is called the *index* of $G$." (Milne, p. 395)

"Tits sketches a proof (corrected in the MR review of the article) that the isomorphism class of $G$ is determined by the isomorphism class of $G_K$, its anisotropic kernel, and its index." (Milne, p. 395)

# Prerequisites

- **Relative root system** — the index encodes the relationship between absolute and relative roots
- **Anisotropic kernel** — one of the three classifying invariants alongside the index
- **Reductive algebraic group** — the index is defined for semisimple groups

# Key Properties

1. The triple $(S, S_0, \text{Galois action})$ encodes the "splitting behavior" of $G$ over $k$
2. $S_0 = \emptyset$ if and only if $G$ is quasi-split
3. $S_0 = S$ if and only if the maximal split torus is central (anisotropic case)
4. The Galois action on $S$ determines whether the form is inner ($\Gamma$ acts trivially) or outer
5. Together with the anisotropic kernel and the absolute type, the index determines $G$

# Construction / Recognition

## To Construct:
1. Choose a maximal split torus $T' \subset G$
2. Choose a maximal torus $T \supset T'$
3. Determine the simple roots $S$ for $(G_{k^{\mathrm{sep}}}, T_{k^{\mathrm{sep}}})$
4. Identify $S_0 = \{\alpha \in S \mid \alpha|_{T'} = 0\}$
5. Compute the action of $\mathrm{Gal}(k^{\mathrm{sep}}/k)$ on $S$
6. The index is the triple $(S, S_0, \text{Galois action})$

# Context & Application

The Tits index is the primary tool for classifying semisimple groups over arbitrary fields. The classification proceeds in two steps: (a) determine the possible indices for each absolute type, and (b) for each index, determine the possible anisotropic kernels. Problem (b) is related to the Brauer group of the field, so a complete solution requires knowledge of $\mathrm{Br}(k)$.

# Examples

**Example 1** (p. 395): For a split group, $S_0 = \emptyset$ and $\Gamma$ acts trivially on $S$, so the index is the Dynkin diagram with no circled vertices.

**Example 2** (p. 395): The classification by Tits (1966) and Selbach (1976) enumerates all possible indices for each type and determines the anisotropic kernels of exceptional type.

# Relationships

## Builds Upon
- **Relative root system** — $S_0$ is defined via the relative vs. absolute roots
- **Anisotropic kernel** — the complementary classifying invariant

## Enables
- **Form of algebraic group** — the index is one of the invariants classifying forms

## Related
- **Inner form** — inner forms have trivial Galois action on $S$
- **Galois cohomology of algebraic groups** — the cohomological classification is related

# Common Errors

- **Error**: Thinking the index alone determines the group
  **Correction**: The index must be supplemented by the anisotropic kernel and the absolute type

# Common Confusions

- **Confusion**: Confusing the Tits index with the Dynkin diagram
  **Clarification**: The Tits index is a Dynkin diagram enriched with the data of $S_0$ (usually shown as circled/uncircled vertices) and the Galois action (shown as arrows)

# Source Reference

Chapter VI: The Structure of Reductive Groups: General Case, Section 3, pages 395-396. References: Tits 1966, Selbach 1976.

# Verification Notes

- Definition source: Direct quote from p. 395
- Confidence: MEDIUM — the section is a summary of Tits's program; full details are in Tits 1966 and Selbach 1976
- Uncertainties: The original proof by Tits had a mistake corrected by Selbach
- Cross-reference status: Verified
