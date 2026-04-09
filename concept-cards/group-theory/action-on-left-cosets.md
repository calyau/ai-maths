---
# === CORE IDENTIFICATION ===
concept: Action on Left Cosets
slug: action-on-left-cosets

# === CLASSIFICATION ===
category: group-actions
subcategory: applications
tier: intermediate

# === PROVENANCE ===
source: "Group Theory"
source_slug: group-theory
authors: "J.S. Milne"
chapter: "Groups Acting on Sets"
chapter_number: 4
pdf_page: 63
section: "Action on the left cosets"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - group-action
  - stabilizer
  - orbit-stabilizer-theorem
extends:
  - group-action
related:
  - cayleys-theorem
  - normal-subgroup
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does G act on the cosets G/H?"
  - "How can the action on cosets detect normal subgroups?"
---

# Quick Definition

$G$ acts on $G/H$ by left multiplication: $g \cdot (aH) = gaH$. The kernel of this action is the largest normal subgroup of $G$ contained in $H$.

# Core Definition

The action of $G$ on $X = G/H$ satisfies: $\operatorname{Stab}(gH) = gHg^{-1}$ and $\ker(G \to \operatorname{Sym}(G/H)) = \bigcap_{g \in G} gHg^{-1}$, the largest normal subgroup of $G$ in $H$ (Milne, p. 63, applying Lemma 4.10).

# Prerequisites

- **Group action** — This is a specific action
- **Stabilizer** — $\operatorname{Stab}(gH) = gHg^{-1}$
- **Orbit-stabilizer theorem** — The action is transitive

# Key Properties

1. The action is always transitive
2. $\operatorname{Stab}(H) = H$; $\operatorname{Stab}(gH) = gHg^{-1}$
3. Kernel = $\bigcap_{g \in G} gHg^{-1}$ = largest normal subgroup in $H$
4. If $H$ contains no nontrivial normal subgroup of $G$, the action is faithful, embedding $G \hookrightarrow S_{(G:H)}$
5. If $|G|$ does not divide $(G:H)!$, then $H$ must contain a nontrivial normal subgroup of $G$

# Context & Application

This action is one of the most versatile tools in group theory. It provides embeddings into symmetric groups smaller than Cayley's theorem, detects normal subgroups, and is used in proofs about groups of specific orders.

# Examples

**Example 1** (p. 63): If $G$ is simple, any proper subgroup $H \neq 1$ gives a faithful action on $G/H$, embedding $G \hookrightarrow S_{(G:H)}$.

**Example 2** (p. 63): A group of order 99 has a subgroup $N$ of order 11. Since $99 \nmid 9!$, $N$ contains a nontrivial normal subgroup; since $|N| = 11$ is prime, $N \trianglelefteq G$.

**Example 3** (p. 63): Groups of order 6: a subgroup $H$ of order 2 either is normal (giving $G \simeq C_6$) or isn't (giving $G \hookrightarrow S_3$, hence $G \simeq S_3$).

# Relationships

## Builds Upon
- **group-action**, **stabilizer**, **orbit-stabilizer-theorem**

## Enables
- Detecting normal subgroups from subgroup indices
- Embedding groups in symmetric groups

# Source Reference

Chapter 4: Groups Acting on Sets, "Action on the left cosets", pages 63-64.

# Verification Notes

- Definition source: Direct from pp. 63-64
- Confidence: HIGH — explicit discussion
- Uncertainties: None
