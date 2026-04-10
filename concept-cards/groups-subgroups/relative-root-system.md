---
# === CORE IDENTIFICATION ===
concept: Relative Root System
slug: relative-root-system

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
  - restricted root system

# === TYPED RELATIONSHIPS ===
prerequisites:
  - root-system
  - reductive-algebraic-group
  - split-maximal-torus
extends:
  - root-system
related:
  - anisotropic-kernel
  - tits-index
contrasts_with:
  - absolute-root-system

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What must I know before understanding arithmetic subgroups?"
---

# Quick Definition

The relative root system of a reductive group $G$ over $k$ is the root system defined using a maximal split torus $T'$ rather than a maximal torus. Unlike the absolute root system, the relative root system may be non-reduced.

# Core Definition

For a reductive group $G$ over $k$, choose a maximal split torus $T'$ and a maximal torus $T \supset T'$. "One defines the root datum much as before — in this case it is not necessarily reduced." (Milne, p. 382)

The relative roots are the nontrivial characters of $T'$ appearing in the adjoint representation of $G$. The simple relative roots form a subset $S$ of the absolute simple roots, and the subset $S_0 \subset S$ of roots vanishing on $T'$ corresponds to the anisotropic kernel.

# Prerequisites

- **Root system** — the relative root system generalizes the absolute root system
- **Reductive algebraic group** — the relative root system is defined for reductive groups
- **Split maximal torus** — the relative roots are characters of the maximal split torus

# Key Properties

1. The relative root system may be non-reduced (e.g., of type $BC_n$)
2. If $G$ is split, the relative root system equals the absolute root system
3. If $G$ is anisotropic (no split torus), the relative root system is empty
4. The subset $S_0$ of simple roots vanishing on $T'$ determines the anisotropic kernel
5. The Galois group $\mathrm{Gal}(k^{\mathrm{sep}}/k)$ acts on the set $S$ of absolute simple roots

# Construction / Recognition

## To Construct:
1. Choose a maximal split torus $T' \subset G$
2. Choose a maximal torus $T \supset T'$
3. Compute the adjoint representation of $T'$ on $\mathrm{Lie}(G)$
4. The nontrivial characters of $T'$ form the relative root system
5. Choose a base $S$ for the absolute roots; the base for relative roots is determined by restriction to $T'$

# Context & Application

The relative root system is essential for understanding non-split reductive groups. It provides structural information about $G$ over $k$ without passing to the algebraic closure, but by its nature it captures only the "split part" of the structure. Together with the anisotropic kernel and the Tits index, it gives a complete classification.

# Examples

**Example 1** (p. 395): For a split group, the maximal split torus is a maximal torus, and the relative root system is the usual (absolute) root system.

**Example 2** (p. 395, from context): For a quasi-split group (one having a Borel subgroup defined over $k$), $S_0 = \emptyset$, meaning the anisotropic kernel is trivial, but the Galois action on $S$ may be nontrivial.

# Relationships

## Builds Upon
- **Root system** — the relative root system is a (possibly non-reduced) root system

## Enables
- **Tits index** — the index records $S$, $S_0$, and the Galois action

## Related
- **Anisotropic kernel** — corresponds to the roots vanishing on the maximal split torus

## Contrasts With
- **Absolute root system** — the root system obtained over $k^{\mathrm{al}}$, which is always reduced

# Common Errors

- **Error**: Assuming the relative root system is always reduced
  **Correction**: The relative root system can be non-reduced (type $BC_n$)

# Common Confusions

- **Confusion**: Confusing relative roots with absolute roots restricted to $T'$
  **Clarification**: The relative roots are indeed restrictions of absolute roots to $T'$, but multiplicities may arise and the system may become non-reduced

# Source Reference

Chapter VI: The Structure of Reductive Groups: General Case, Section 3, pages 395-396.

# Verification Notes

- Definition source: Synthesized from pp. 382, 395
- Confidence: MEDIUM — the section is a brief overview referencing Tits 1966; definitions are stated but not fully developed
- Uncertainties: Detailed construction references Tits 1966 and Selbach 1976
- Cross-reference status: Verified
