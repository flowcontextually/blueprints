# System: Web Browser

This is a core system blueprint that enables the `cx-shell` to launch and control a local web browser for stateful UI automation.

It does not connect to an external API but instead configures the built-in `browser-declarative` engine.

## Configuration

When you create a connection using this blueprint, you will be asked for the following details:

-   **Browser:** The browser to use. Can be `chromium`, `firefox`, or `webkit`.
-   **Run in headless mode?:** If `true`, the browser will run in the background without a visible UI. Set to `false` for debugging to watch the automation happen live.

This blueprint does not require a `schemas.py` file, as all of its actions (`browser_navigate`, `browser_click`, etc.) are natively defined within the `cx-core-schemas` library and are handled directly by the shell's ScriptEngine.
