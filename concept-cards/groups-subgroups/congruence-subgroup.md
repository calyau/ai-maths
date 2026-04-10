---
# === CORE IDENTIFICATION ===
concept: Congruence Subgroup
slug: congruence-subgroup

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
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - principal-congruence-subgroup
  - arithmetic-subgroup
extends:
  - arithmetic-subgroup
related:
  - congruence-subgroup-problem
  - adelic-description-of-congruence-subgroups
contrasts_with:
  - arithmetic-subgroup

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a congruence subgroup?"
  - "What distinguishes an arithmetic subgroup from a congruence subgroup?"
---

# Quick Definition

A congruence subgroup of $G(\mathbb{Q})$ is any subgroup containing some principal congruence subgroup $\Gamma(N)$ as a subgroup of finite index. Every congruence subgroup is arithmetic, but the converse fails for some groups.

# Core Definition

"A *congruence subgroup* of $G(\mathbb{Q})$ is any subgroup containing some $\Gamma(N)$ as a subgroup of finite index, so congruence subgroups are arithmetic subgroups." (Milne, p. 398)

Equivalently, by the adelic description (Proposition 6.1), congruence subgroups are exactly the subgroups of the form $K \cap G(\mathbb{Q})$ for compact open subgroups $K$ of $G(\mathbb{A}_f)$.

# Prerequisites

- **Principal congruence subgroup** — congruence subgroups are defined in terms of these
- **Arithmetic subgroup** — every congruence subgroup is arithmetic

# Key Properties

1. Every congruence subgroup is arithmetic
2. Not every arithmetic subgroup is congruence (for $\mathrm{SL}_2$, Klein 1880)
3. For $\mathrm{SL}_n$ ($n \geq 3$) and $\mathrm{Sp}_{2n}$ ($n \geq 2$), all arithmetic subgroups are congruence
4. The image of a congruence subgroup under an isogeny need not be congruence
5. Congruence subgroups correspond bijectively to compact open subgroups of $G(\mathbb{A}_f)$ (Proposition 6.1)
6. The set of congruence subgroups is independent of the choice of representation and lattice (Section 4)

# Construction / Recognition

## To Construct:
1. Choose a faithful representation $G \hookrightarrow \mathrm{GL}_n$
2. Take a principal congruence subgroup $\Gamma(N) = \ker(G(\mathbb{Z}) \to G(\mathbb{Z}/N\mathbb{Z}))$
3. Any subgroup of $G(\mathbb{Q})$ containing $\Gamma(N)$ with finite index is a congruence subgroup

## To Recognize:
1. Check if the subgroup contains some $\Gamma(N)$ as a subgroup of finite index
2. Alternatively, check if it arises as $K \cap G(\mathbb{Q})$ for a compact open $K \subset G(\mathbb{A}_f)$

# Context & Application

Congruence subgroups arise naturally in number theory: congruence conditions modulo $N$ on matrix entries define subgroups of $\mathrm{GL}_n(\mathbb{Z})$. The congruence subgroup problem asks whether all arithmetic subgroups are congruence, and the answer depends fundamentally on the group $G$.

# Examples

**Example 1** (p. 398): $\Gamma_0(N) = \left\{\begin{pmatrix} a & b \\ c & d\end{pmatrix} \in \mathrm{SL}_2(\mathbb{Z}) \mid N \mid c\right\}$ is a congruence subgroup of $\mathrm{SL}_2(\mathbb{Q})$ (mentioned in Section 16).

**Example 2** (p. 409): For $\mathrm{SL}_2$, there exist arithmetic subgroups that are not congruence. In fact, if $N(m)$ is the number of congruence subgroups of index $\leq m$ and $N'(m)$ the number of arithmetic subgroups, then $N(m)/N'(m) \to 0$ as $m \to \infty$.

# Relationships

## Builds Upon
- **Principal congruence subgroup** — congruence subgroups contain a $\Gamma(N)$
- **Arithmetic subgroup** — congruence subgroups are a subclass of arithmetic subgroups

## Enables
- **Congruence subgroup problem** — asks when all arithmetic subgroups are congruence
- **Connected Shimura variety** — defined using congruence subgroups (Theorem 16.4)
- **Adelic description of congruence subgroups** — the adelic characterization

## Contrasts With
- **Arithmetic subgroup** — congruence subgroups are a proper subclass for some groups

# Common Errors

- **Error**: Assuming all arithmetic subgroups of $\mathrm{SL}_2(\mathbb{Z})$ are congruence
  **Correction**: $\mathrm{SL}_2$ is a prominent example where non-congruence arithmetic subgroups exist

# Common Confusions

- **Confusion**: Thinking the distinction between arithmetic and congruence is merely technical
  **Clarification**: The congruence subgroup problem is a deep question with connections to the theory of automorphic forms and the Langlands program

# Source Reference

Chapter VII: Arithmetic Subgroups, Section 2, page 398. Section 14 for the congruence subgroup problem.

# Verification Notes

- Definition source: Direct quote from p. 398
- Confidence: HIGH — explicit definition
- Uncertainties: None
- Cross-reference status: Verified
