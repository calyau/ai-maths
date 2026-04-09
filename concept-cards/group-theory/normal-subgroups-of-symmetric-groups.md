---
# === CORE IDENTIFICATION ===
concept: Normal Subgroups of Symmetric Groups
slug: normal-subgroups-of-symmetric-groups

# === CLASSIFICATION ===
category: group-actions
subcategory: permutation-groups
tier: intermediate

# === PROVENANCE ===
source: "Group Theory"
source_slug: group-theory
authors: "J.S. Milne"
chapter: "Groups Acting on Sets"
chapter_number: 4
pdf_page: 69
section: "Permutation groups"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - simplicity-of-alternating-groups
  - symmetric-group
extends: []
related:
  - normal-subgroup
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What are the normal subgroups of S_n?"
---

# Quick Definition

For $n \geq 5$, the only normal subgroups of $S_n$ are $\{1\}$, $A_n$, and $S_n$.

# Core Definition

"For $n \geq 5$, the only normal subgroups of $S_n$ are $1$, $A_n$, and $S_n$" (Milne, Corollary 4.37, p. 69).

# Prerequisites

- **Simplicity of alternating groups** — Uses $A_n$ is simple for $n \geq 5$
- **Symmetric group** — The group whose normal subgroups are classified

# Key Properties

1. If $N \trianglelefteq S_n$ then $N \cap A_n \trianglelefteq A_n$
2. Since $A_n$ is simple ($n \geq 5$): $N \cap A_n = A_n$ or $N \cap A_n = \{1\}$
3. First case: $N \supset A_n$, so $N = A_n$ or $S_n$
4. Second case: $N$ embeds in $S_n/A_n \simeq C_2$, so $|N| \leq 2$; but no conjugacy class in $S_n$ (other than $\{1\}$) has size 1, so $N = \{1\}$

# Examples

**Example 1** (p. 68): For $S_4$: $A_4$ has a normal subgroup $V \simeq C_2 \times C_2$. So $S_4$ has normal subgroups $\{1\}, V, A_4, S_4$. This shows the result requires $n \geq 5$.

# Relationships

## Builds Upon
- **simplicity-of-alternating-groups**

# Source Reference

Chapter 4: Groups Acting on Sets, Corollary 4.37, page 69.

# Verification Notes

- Definition source: Corollary 4.37, p. 69
- Confidence: HIGH — explicit theorem
- Uncertainties: None
