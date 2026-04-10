---
# === CORE IDENTIFICATION ===
concept: Congruence Subgroup Problem
slug: congruence-subgroup-problem

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
pdf_page: 409
section: "The congruence subgroup problem"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - CSP

# === TYPED RELATIONSHIPS ===
prerequisites:
  - arithmetic-subgroup
  - congruence-subgroup
  - principal-congruence-subgroup
extends: []
related:
  - congruence-kernel
  - margulis-arithmeticity-theorem
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What distinguishes an arithmetic subgroup from a congruence subgroup?"
---

# Quick Definition

The congruence subgroup problem asks: for which algebraic groups $G$ is every arithmetic subgroup a congruence subgroup? For $\mathrm{SL}_2$, the answer is no (Klein, 1880), but for $\mathrm{SL}_n$ ($n \geq 3$) and $\mathrm{Sp}_{2n}$ ($n \geq 2$), the answer is yes.

# Core Definition

"Consider an algebraic subgroup $G$ of $\mathrm{GL}_n$. Is every arithmetic subgroup congruence? That is, does every subgroup commensurable with $G(\mathbb{Z})$ contain $\Gamma(N) \stackrel{\text{def}}{=} \ker(G(\mathbb{Z}) \to G(\mathbb{Z}/N\mathbb{Z}))$ for some $N$." (Milne, p. 409)

The modern formulation: the arithmetic and congruence subgroups define topologies on $G(\mathbb{Q})$ with completions $\hat{G}$ and $\bar{G}$. The kernel $C(G)$ of $\hat{G} \to \bar{G}$ is the *congruence kernel*. The modern problem is to compute $C(G)$. $C(G) = 1$ iff all arithmetic subgroups are congruence.

# Prerequisites

- **Arithmetic subgroup** — one side of the comparison
- **Congruence subgroup** — the other side
- **Principal congruence subgroup** — the defining objects for congruence subgroups

# Key Properties

1. $\mathrm{SL}_2(\mathbb{Z})$ has non-congruence arithmetic subgroups (Klein, 1880)
2. For $\mathrm{SL}_2$, congruence subgroups are sparse: $N(m)/N'(m) \to 0$ as $m \to \infty$
3. For $\mathrm{SL}_n$ ($n \geq 3$), $\mathrm{Sp}_{2n}$ ($n \geq 2$): all arithmetic subgroups are congruence
4. The image of a congruence subgroup under an isogeny need not be congruence
5. $C(G)$ is finite iff it is contained in the centre of $\widehat{G(\mathbb{Q})}$
6. For simply connected $G$ and $G' = G/N$ with $N \neq 1$: $C(G')$ is infinite (contains $N(\mathbb{A}_f)/N(\mathbb{Q})$)
7. There is a precise conjecture predicting when $C(G)$ is finite and its structure

# Construction / Recognition

## To Determine if All Arithmetic Subgroups are Congruence:
1. Check if $C(G) = 1$
2. For simply connected, almost-simple groups: the answer depends on the type and rank
3. $\mathrm{SL}_2$ (rank 1): $C(G)$ is infinite
4. $\mathrm{SL}_n$ ($n \geq 3$), $\mathrm{Sp}_{2n}$ ($n \geq 2$): $C(G) = 1$

# Context & Application

The congruence subgroup problem is one of the central problems in the theory of arithmetic groups. It connects to the Langlands program (automorphic forms are naturally associated to congruence subgroups), the theory of Shimura varieties (which use congruence subgroups), and the metaplectic kernel (which gives the structure of $C(G)$ when finite).

# Examples

**Example 1** (p. 409): $\mathrm{SL}_2(\mathbb{Z})$ has infinitely many subgroups of finite index that are not congruence. The proof uses the presentation $\mathrm{SL}_2(\mathbb{Z})/\{\pm I\} \cong \mathbb{Z}/2 * \mathbb{Z}/3$ to construct non-congruence quotients.

**Example 2** (p. 409): For simply connected $G$ and $G' = G/N$: the isogeny $G \to G'$ does not map congruence subgroups to congruence subgroups because $\ker(\bar{\pi}) = N(\mathbb{A}_f) \neq N(\mathbb{Q}) = \ker(\hat{\pi})$.

# Relationships

## Builds Upon
- **Arithmetic subgroup** — one side of the CSP comparison
- **Congruence subgroup** — the other side

## Enables
- **Congruence kernel** — the modern formulation of the problem

## Related
- **Margulis arithmeticity theorem** — both address the structure of discrete subgroups

# Common Errors

- **Error**: Assuming all arithmetic subgroups are congruence because of the result for $\mathrm{SL}_n$ ($n \geq 3$)
  **Correction**: The result depends on the group; $\mathrm{SL}_2$ is a counterexample

# Common Confusions

- **Confusion**: Thinking the classical and modern congruence subgroup problems are the same
  **Clarification**: The classical problem asks yes/no (is every arithmetic subgroup congruence?); the modern problem asks for the structure of the congruence kernel $C(G)$

# Source Reference

Chapter VII: Arithmetic Subgroups, Section 14, pages 409-410.

# Verification Notes

- Definition source: Direct quote from p. 409
- Confidence: HIGH — explicit problem statement with examples
- Uncertainties: None
- Cross-reference status: Verified
