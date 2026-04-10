---
# === CORE IDENTIFICATION ===
concept: Arithmetic Subgroup
slug: arithmetic-subgroup

# === CLASSIFICATION ===
category: arithmetic-groups
subcategory: null
tier: advanced

# === PROVENANCE ===
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "Arithmetic Subgroups"
chapter_number: 7
pdf_page: 398
section: "Definitions and examples"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - arithmetic group

# === TYPED RELATIONSHIPS ===
prerequisites:
  - algebraic-group
  - commensurable-subgroups
extends: []
related:
  - congruence-subgroup
  - principal-congruence-subgroup
  - lattice-in-lie-group
  - arithmetic-subgroup-of-lie-group
contrasts_with:
  - congruence-subgroup

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an arithmetic subgroup?"
  - "What must I know before understanding arithmetic subgroups?"
  - "What distinguishes an arithmetic subgroup from a congruence subgroup?"
  - "How do arithmetic subgroups relate to discrete subgroups of Lie groups?"
---

# Quick Definition

An arithmetic subgroup of $G(\mathbb{Q})$, where $G$ is an algebraic group over $\mathbb{Q}$, is any subgroup commensurable with $G(\mathbb{Q})_L = \{g \in G(\mathbb{Q}) \mid \rho(g)L = L\}$ for a faithful representation $\rho: G \to \mathrm{GL}_V$ and lattice $L \subset V$.

# Core Definition

Let $G$ be an algebraic group over $\mathbb{Q}$, $\rho: G \to \mathrm{GL}_V$ a faithful representation on a finite-dimensional vector space $V$, and $L$ a lattice in $V$. Define $G(\mathbb{Q})_L = \{g \in G(\mathbb{Q}) \mid \rho(g)L = L\}$.

"An *arithmetic subgroup* of $G(\mathbb{Q})$ is any subgroup commensurable with $G(\mathbb{Q})_L$." (Milne, p. 398)

This definition is independent of the choice of $\rho$ and $L$ (Proposition 4.2, p. 399).

# Prerequisites

- **Algebraic group** — arithmetic subgroups are defined for algebraic groups over $\mathbb{Q}$
- **Commensurable subgroups** — the definition uses commensurability

# Key Properties

1. The notion is independent of the faithful representation $\rho$ and lattice $L$ (Proposition 4.2)
2. Arithmetic subgroups are discrete in $G(\mathbb{R})$ (Section 7)
3. For a homomorphism $\varphi: G \to G'$, the image $\varphi(\Gamma)$ of an arithmetic subgroup $\Gamma$ is contained in an arithmetic subgroup of $G'(\mathbb{Q})$ (Proposition 5.2)
4. If $\varphi$ is a quotient map, $\varphi(\Gamma)$ is of finite index in an arithmetic subgroup (Remark 5.3)
5. Every arithmetic subgroup contains a torsion-free subgroup of finite index (Theorem 8.1)
6. Every congruence subgroup is arithmetic, but the converse fails in general

# Construction / Recognition

## To Construct:
1. Choose a faithful representation $\rho: G \to \mathrm{GL}_n$
2. Take $L = \mathbb{Z}^n$ as the standard lattice
3. Then $G(\mathbb{Q})_L = G(\mathbb{Q}) \cap \mathrm{GL}_n(\mathbb{Z})$
4. Any subgroup commensurable with this is arithmetic

## To Recognize:
1. Embed $G$ into $\mathrm{GL}_n$ via a faithful representation
2. Check if the subgroup is commensurable with $G(\mathbb{Q}) \cap \mathrm{GL}_n(\mathbb{Z})$

# Context & Application

Arithmetic subgroups are the fundamental discrete subgroups in the study of algebraic groups over number fields. They provide discrete groups acting on symmetric spaces, yielding locally symmetric manifolds and moduli spaces. The remarkable theorem of Margulis shows that for most semisimple Lie groups, *all* lattices are arithmetic.

# Examples

**Example 1** (p. 398): $\mathrm{GL}_n(\mathbb{Z}) = \{A \in M_n(\mathbb{Z}) \mid \det(A) = \pm 1\}$ is an arithmetic subgroup of $\mathrm{GL}_n(\mathbb{Q})$.

**Example 2** (p. 398): $\mathrm{Sp}_{2n}(\mathbb{Z})$ is an arithmetic subgroup of $\mathrm{Sp}_{2n}(\mathbb{Q})$, and all arithmetic subgroups of $\mathrm{Sp}_{2n}(\mathbb{Q})$ are commensurable with it.

**Example 3** (p. 398): Arithmetic subgroups can be finite. For $G = \mathbb{G}_m$, $G(\mathbb{Z}) = \{\pm 1\}$.

**Example 4** (p. 398): For a number field $K/\mathbb{Q}$ and the torus $T = (\mathbb{G}_m)_{K/\mathbb{Q}}$, $T(\mathbb{Z})$ is the group of units $U_K$.

# Relationships

## Builds Upon
- **Commensurable subgroups** — arithmetic subgroups are a commensurability class
- **Algebraic group** — defined for algebraic groups over $\mathbb{Q}$

## Enables
- **Congruence subgroup problem** — asks whether all arithmetic subgroups are congruence
- **Shimura varieties** — defined using arithmetic subgroups
- **Reduction theory** — studies the geometry of $\Gamma \backslash G(\mathbb{R})$

## Related
- **Lattice in Lie group** — arithmetic subgroups are lattices in $G(\mathbb{R})$
- **Arithmetic subgroup of Lie group** — the more general notion

## Contrasts With
- **Congruence subgroup** — every congruence subgroup is arithmetic, but not conversely

# Common Errors

- **Error**: Defining arithmetic subgroups as $G(\mathbb{Z})$ without specifying a representation
  **Correction**: $G(\mathbb{Z})$ depends on a choice of embedding $G \hookrightarrow \mathrm{GL}_n$; the commensurability class is independent

# Common Confusions

- **Confusion**: Thinking arithmetic subgroups and congruence subgroups are the same
  **Clarification**: Congruence subgroups are arithmetic, but $\mathrm{SL}_2(\mathbb{Z})$ has arithmetic subgroups that are not congruence (Klein, 1880)

# Source Reference

Chapter VII: Arithmetic Subgroups, Section 2, pages 398-399. Examples 2.1-2.6, Proposition 4.2.

# Verification Notes

- Definition source: Direct quote from p. 398
- Confidence: HIGH — explicit definition with many examples
- Uncertainties: None
- Cross-reference status: Verified
