## Simple install

Codelab is herE:

Ensure the execution is as simple as it gets.

- Fewer words are better than many words.
- Fewer steps are better.
- Fewer dependencies are better.
- If a script is in the Cloud Shell, we can leverage it. If it's not, its additional friction.

### uv: the exception

The only exception is (IMHO) `uv`.

`uv` while not needed ensures the same execution experience between human and machine (ie, Gemini CLI). Python tends to be very ENV-dependent and `<virtualenv>` only works if you remember to activate it with `<source .env/bin/activate>`. This is what Im trying to fix by usign the same. Of course I'm open to alternatives. We could also say "If you are a python pro, just use whatever you're used to, but ensure to instruct GEmini CLI to use python the same you use it".

## DONTs

- Ensure `just` and `justfiles` are missing. The original repo had it, but we dont want it.
