The workshop is here: https://codelabs.developers.google.com/codelabs/build-a-simple-travel-agent-with-adk-and-gemini-cli

Read it.

## Code before and after

[OLD] The workshop and code used to be here: https://github.com/palladius/ai-friendly-agents/tree/main/adk/workshops/simple-travel-agent

[NEW] It is now here: https://github.com/google/adk-gemini-cli-workshop

Ensure the codelab ONLY points to new code.

The only exception is code snippets in an issue (I dont want to move issues).

Note there are intrinsic differences between the two repos:

1. One was in a subfolder, the new one is in the root folder (this is GOOD).
2. The old one has some branches which can be used for advanced solutions. We might want to find and move those in a way or another. Probably it's still ok to point to other repo if the behaviour is "expert-only" and obscure, meaning this wouldnt be the classic "beginner" user and well beaten track.
3. The old one has a `justfile` which is not present in the new one. This is ok - its the old version. The new needs to port to Makefile all just commands.

## What we want

Before and foremost, **we want to ensure a smooth experience for codelab users**.
