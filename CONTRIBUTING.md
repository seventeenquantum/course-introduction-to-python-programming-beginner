# Contributing — 17 Quantum Course Repositories

This document covers everything you need to fork a course repo, complete the exercises, and submit your work correctly.

---

## Prerequisites

Before you begin, make sure you have:

- A [GitHub account](https://github.com/signup)
- Git installed on your machine — [git-scm.com](https://git-scm.com)
- Any course-specific tooling listed in this repo's `README.md`

---

## Submission Workflow

### 1. Fork the repository

Click **Fork** at the top right of this page. This creates a personal copy of the course repo under your GitHub account.

### 2. Clone your fork

```bash
git clone https://github.com/<your-username>/<course-repo>.git
cd <course-repo>
```

### 3. Add the upstream remote

This keeps your fork connected to the original course repo so you can pull updates.

```bash
git remote add upstream https://github.com/17quantum/<course-repo>.git
```

Verify your remotes:

```bash
git remote -v
# origin    https://github.com/<your-username>/<course-repo>.git (fetch)
# origin    https://github.com/<your-username>/<course-repo>.git (push)
# upstream  https://github.com/17quantum/<course-repo>.git (fetch)
# upstream  https://github.com/17quantum/<course-repo>.git (push)
```

### 4. Create a submission branch

Always work on a dedicated branch — never commit directly to `main`.

```bash
git checkout -b submission/<your-full-name>

# Example:
git checkout -b submission/amara-okafor
```

### 5. Complete the exercises

Work through the exercises inside the `exercises/` directory. Each exercise folder contains:

- `README.md` — the brief, requirements, and acceptance criteria
- `src/` — starter files with clearly marked `TODO` comments

Do not modify anything outside of `exercises/`. Do not delete or rename existing files unless the exercise brief explicitly instructs you to.

### 6. Commit your work

Write clear, descriptive commit messages.

```bash
git add .
git commit -m "feat: complete exercise 01 - <exercise title>"
```

Use one commit per exercise where possible. Avoid single commits that cover the entire course.

### 7. Push your branch

```bash
git push origin submission/<your-full-name>
```

### 8. Open a pull request

1. Go to the **upstream** course repo on GitHub: `github.com/17quantum/<course-repo>`
2. Click **Pull requests → New pull request**
3. Set the base to `main` on the upstream repo
4. Set the compare to `submission/<your-full-name>` on your fork
5. Fill in the pull request template fully — incomplete submissions will be returned
6. Click **Create pull request**

---

## Pulling Course Updates

If the course material is updated after you fork, sync your fork before continuing:

```bash
git fetch upstream
git checkout main
git merge upstream/main
git checkout submission/<your-full-name>
git rebase main
```

---

## Reviewing the Solution

The `solution` branch contains the completed reference implementation. Consult it **after** you have submitted your pull request — not before. Using the solution branch before submitting defeats the purpose of the exercise and limits your own learning.

```bash
git fetch upstream
git checkout upstream/solution -- exercises/<exercise-folder>/
```

---

## Code Standards

- Follow the conventions and patterns established in the starter code
- Remove all `console.log` / debug statements before submitting
- Do not submit code that throws errors or fails to run
- If an exercise is incomplete, note it explicitly in your PR description with what you attempted and where you got stuck

---

## Getting Help

If you are stuck on an exercise:

1. Re-read the exercise `README.md` carefully
2. Check the course material on [education.17quantum.com](https://education.17quantum.com)
3. Ask in the learner community — linked on the platform
4. Open a GitHub **Issue** on this repo using the `question` label — do not open a PR to ask a question

---

## What Happens After You Submit

A 17 Quantum instructor will review your pull request and leave feedback as inline comments. You may be asked to make changes — push new commits to your branch and they will appear in the open PR automatically.

Once your submission is accepted, the PR will be closed. You do not need to delete your fork.

---

## Rules

- One fork per learner per course
- One pull request per learner — do not close and reopen
- Do not copy another learner's submission
- Do not open pull requests on the `solution` branch
