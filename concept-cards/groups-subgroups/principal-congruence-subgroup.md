---
# === CORE IDENTIFICATION ===
concept: Principal Congruence Subgroup
slug: principal-congruence-subgroup

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
  - "Gamma(N)"
  - principal congruence subgroup of level N

# === TYPED RELATIONSHIPS ===
prerequisites:
  - arithmetic-subgroup
extends:
  - arithmetic-subgroup
related:
  - congruence-subgroup
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a congruence subgroup?"
  - "What distinguishes an arithmetic subgroup from a congruence subgroup?"
---

# Quick Definition

The principal congruence subgroup of level $N$ is $\Gamma(N)_L = \{g \in G(\mathbb{Q})_L \mid g \text{ acts as } 1 \text{ on } L/NL\}$, the kernel of the reduction map $G(\mathbb{Q})_L \to \mathrm{Aut}(L/NL)$. It is a normal subgroup of finite index in $G(\mathbb{Q})_L$.

# Core Definition

For an algebraic group $G$ over $\mathbb{Q}$ with faithful representation $\rho: G \to \mathrm{GL}_V$ and lattice $L \subset V$, "for an integer $N > 1$, the *principal congruence subgroup of level* $N$ is $\Gamma(N)_L = \{g \in G(\mathbb{Q})_L \mid g \text{ acts as } 1 \text{ on } L/NL\}$." (Milne, p. 398)

Equivalently, $\Gamma(N)_L$ is the kernel of $G(\mathbb{Q})_L \to \mathrm{Aut}(L/NL)$.

# Prerequisites

- **Arithmetic subgroup** — $\Gamma(N)$ is a specific arithmetic subgroup

# Key Properties

1. $\Gamma(N)_L$ is a normal subgroup of $G(\mathbb{Q})_L$
2. $\Gamma(N)_L$ has finite index in $G(\mathbb{Q})_L$ (since $\mathrm{Aut}(L/NL)$ is finite)
3. $\Gamma(N)$ is torsion-free for $N \geq 3$ when $G \subset \mathrm{GL}_n$ (Lemma 8.2)
4. $\Gamma(N) \subset \Gamma(M)$ when $M | N$

# Construction / Recognition

## To Construct:
1. Choose a faithful representation $G \hookrightarrow \mathrm{GL}_n$ and lattice $L = \mathbb{Z}^n$
2. $\Gamma(N) = \{A \in G(\mathbb{Q}) \cap \mathrm{GL}_n(\mathbb{Z}) \mid A \equiv I \bmod N\}$
3. Equivalently, $\Gamma(N) = \ker(G(\mathbb{Z}) \to G(\mathbb{Z}/N\mathbb{Z}))$

# Context & Application

Principal congruence subgroups are the building blocks of congruence subgroups: a congruence subgroup is any subgroup containing some $\Gamma(N)$ as a subgroup of finite index. They provide a natural filtration of arithmetic subgroups by level.

# Examples

**Example 1** (p. 398): For $G = \mathrm{GL}_n$, $\Gamma(N) = \{A \in \mathrm{GL}_n(\mathbb{Z}) \mid A \equiv I \bmod N\} = \ker(\mathrm{GL}_n(\mathbb{Z}) \to \mathrm{GL}_n(\mathbb{Z}/N\mathbb{Z}))$.

**Example 2** (p. 398): For a subgroup $G \subset \mathrm{GL}_n$, $\Gamma(N)$ for $G$ is $G(\mathbb{Q}) \cap \Gamma(N)_{\mathrm{GL}_n}$.

# Relationships

## Builds Upon
- **Arithmetic subgroup** — $\Gamma(N)$ is a specific arithmetic subgroup

## Enables
- **Congruence subgroup** — defined as subgroups containing some $\Gamma(N)$
- **Torsion-free arithmetic group** — $\Gamma(p)$ is torsion-free for primes $p \geq 3$
- **Congruence subgroup problem** — asks whether all arithmetic subgroups contain some $\Gamma(N)$

# Common Errors

- **Error**: Forgetting that $\Gamma(N)$ depends on the choice of representation and lattice
  **Correction**: The specific group $\Gamma(N)$ depends on $\rho$ and $L$, but the set of congruence subgroups does not (Section 4)

# Common Confusions

- **Confusion**: Thinking $\Gamma(N)$ is the same for all representations
  **Clarification**: The group $\Gamma(N)_L$ depends on the lattice $L$, but for any two choices, the resulting sets of congruence subgroups are the same

# Source Reference

Chapter VII: Arithmetic Subgroups, Section 2, page 398. Example 2.1.

# Verification Notes

- Definition source: Direct quote from p. 398
- Confidence: HIGH — explicit definition
- Uncertainties: None
- Cross-reference status: Verified
