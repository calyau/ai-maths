---
# === CORE IDENTIFICATION ===
concept: Geometrically Almost-Simple Group
slug: geometrically-almost-simple-group

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
pdf_page: 392
section: "Reductive algebraic groups"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - absolutely almost-simple group

# === TYPED RELATIONSHIPS ===
prerequisites:
  - reductive-algebraic-group
  - weil-restriction-of-scalars
extends:
  - reductive-algebraic-group
related:
  - inner-form
  - tits-index
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does Galois cohomology classify forms of algebraic groups?"
---

# Quick Definition

A group $G$ over $k$ is geometrically almost-simple if it is almost-simple and remains almost-simple over $k^{\mathrm{al}}$ (i.e., it does not decompose into a product of simpler groups after base change). The classification of semisimple groups reduces to this case via Weil restriction.

# Core Definition

For a simply connected semisimple group $G$ over $k$, the decomposition $G_{k^{\mathrm{al}}} = G_1 \times \cdots \times G_r$ into almost-simple factors is permuted by $\Gamma = \mathrm{Gal}(k^{\mathrm{al}}/k)$. If $\Gamma$ acts transitively on $\{G_1, \ldots, G_r\}$, then $G$ is almost-simple over $k$. "The group $G_1$ over $K$ is **geometrically almost-simple**, i.e., it is almost-simple and remains almost-simple over $k^{\mathrm{al}}$." (Milne, p. 392)

Every almost-simple group $G$ over $k$ is isomorphic to the Weil restriction $G_{1*}$ of a geometrically almost-simple group $G_1$ over a subfield $K$ of $k^{\mathrm{al}}$ (Proposition 1.19).

# Prerequisites

- **Reductive algebraic group** — geometrically almost-simple groups are a special class
- **Weil restriction of scalars** — the reduction to the geometrically almost-simple case uses Weil restriction

# Key Properties

1. $G$ is geometrically almost-simple iff $G_{k^{\mathrm{al}}}$ is almost-simple
2. Every almost-simple group is a Weil restriction of a geometrically almost-simple group (Proposition 1.19)
3. $H^1(k, G) \simeq H^1(K, G_1)$ by Shapiro's lemma when $G \simeq G_{1*}$
4. The classification of semisimple groups reduces to the geometrically almost-simple case

# Construction / Recognition

## To Recognize:
1. Check that $G$ is almost-simple over $k$
2. Check that $G_{k^{\mathrm{al}}}$ remains almost-simple (does not split into a product)

## Reduction to Geometrically Almost-Simple:
1. Decompose $G_{k^{\mathrm{al}}} = G_1 \times \cdots \times G_r$
2. Group the factors by $\Gamma$-orbits: $G = H_1 \times \cdots \times H_s$
3. Each $H_j$ is almost-simple over $k$ and $H_j \simeq (G_{j1})_*$ for a geometrically almost-simple $G_{j1}$

# Context & Application

The reduction to geometrically almost-simple groups is a key simplification in the classification of semisimple groups. It means one only needs to classify forms of the groups corresponding to each indecomposable Dynkin diagram.

# Examples

**Example 1** (p. 392): $\mathrm{SL}_n$ is geometrically almost-simple: it is almost-simple over any field and $(\mathrm{SL}_n)_{k^{\mathrm{al}}}$ remains almost-simple.

**Example 2** (p. 392): If $K/k$ is quadratic and $G_1 = \mathrm{SL}_n$ over $K$, then $G = (G_1)_{K/k}$ is almost-simple over $k$ but not geometrically almost-simple: $G_{k^{\mathrm{al}}} \simeq \mathrm{SL}_n \times \mathrm{SL}_n$.

# Relationships

## Builds Upon
- **Reductive algebraic group** — a special class of semisimple groups

## Enables
- **Inner form** — inner/outer form classification is done for geometrically almost-simple groups
- **Tits index** — the index is defined for these groups

## Related
- **Weil restriction of scalars** — connects almost-simple to geometrically almost-simple

# Common Errors

- **Error**: Assuming "almost-simple over $k$" implies "geometrically almost-simple"
  **Correction**: $G$ can be almost-simple over $k$ while $G_{k^{\mathrm{al}}}$ splits into a product

# Common Confusions

- **Confusion**: Confusing "simple" with "almost-simple"
  **Clarification**: Almost-simple means the only proper normal subgroups are finite (contained in the centre); simple means no proper normal subgroups at all

# Source Reference

Chapter VI: The Structure of Reductive Groups: General Case, Section 1d, pages 391-393. Proposition 1.19.

# Verification Notes

- Definition source: Direct quote from p. 392
- Confidence: HIGH — explicit definition
- Uncertainties: None
- Cross-reference status: Verified
