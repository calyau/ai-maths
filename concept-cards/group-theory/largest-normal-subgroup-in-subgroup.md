---
# === CORE IDENTIFICATION ===
concept: Largest Normal Subgroup in a Subgroup
slug: largest-normal-subgroup-in-subgroup

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
pdf_page: 60
section: "Transitive actions"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - normal-subgroup
  - stabilizer
  - action-on-left-cosets
extends: []
related:
  - kernel-of-action
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the largest normal subgroup of G contained in a given subgroup H?"
---

# Quick Definition

For any subgroup $H$ of $G$, $\bigcap_{g \in G} gHg^{-1}$ is the largest normal subgroup of $G$ contained in $H$.

# Core Definition

"For any subgroup $H$ of a group $G$, $\bigcap_{g \in G} gHg^{-1}$ is the largest normal subgroup contained in $H$" (Milne, Lemma 4.10, p. 60). This equals the kernel of the action of $G$ on $G/H$.

# Prerequisites

- **Normal subgroup** — The object being characterized
- **Stabilizer** — $\operatorname{Stab}(gH) = gHg^{-1}$
- **Action on left cosets** — The kernel equals this intersection

# Key Properties

1. $N_0 = \bigcap_{g \in G} gHg^{-1}$ is a normal subgroup of $G$
2. $N_0 \subset H$
3. Any normal subgroup $N \trianglelefteq G$ with $N \subset H$ satisfies $N \subset N_0$
4. $N_0 = \ker(G \to \operatorname{Sym}(G/H))$

# Context & Application

This is the key tool for detecting normal subgroups. If $|G|$ does not divide $(G:H)!$, then the kernel must be nontrivial, forcing $H$ to contain a nontrivial normal subgroup.

# Relationships

## Related
- **kernel-of-action** — The kernel of the coset action equals this intersection
- **action-on-left-cosets** — The practical application

# Source Reference

Chapter 4: Groups Acting on Sets, Lemma 4.10, page 60.

# Verification Notes

- Definition source: Lemma 4.10, p. 60
- Confidence: HIGH — explicit lemma with proof
- Uncertainties: None
