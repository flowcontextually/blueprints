# Contextually Blueprints

Welcome to the official standard library of blueprints for the **Contextually** platform! This repository is the central, version-controlled "knowledge base" for the entire ecosystem.

Blueprints are the heart of Contextually. They are self-contained, versioned packages that contain the "knowledge" of how to interact with an external service, like a REST API or a database. The `cx` shell uses these blueprints to provide its dynamic, interactive capabilities.

[**Learn more about the Blueprint Ecosystem in our official documentation.**](https://flowcontextually.github.io/docs/explanation/blueprint-ecosystem/)

---

## 🚀 Using Blueprints

You don't need to clone this repository to use these blueprints! The `cx` shell automatically downloads and caches them on-demand the first time you use them.

To use a blueprint, simply create a connection that references the blueprint's ID. The easiest way is with the `cx connection create` command. For example, to create a connection for the Microsoft SQL Server blueprint:

```bash
cx connection create --blueprint "system/mssql@v0.1.1"
```

The `cx` shell will automatically download the `v0.1.1` release and guide you through the setup.

## 📦 Available Blueprints

This is a living catalog of the official and community-vetted blueprints.

### System Blueprints (`system/`)

These are core blueprints maintained directly by the Contextually team.

| Blueprint                         | Latest Version | Description                                                            |
| :-------------------------------- | :------------- | :--------------------------------------------------------------------- |
| [`system/mssql`](./system/mssql/) | `v0.1.1`       | Provides connectivity and query capabilities for Microsoft SQL Server. |

### Community Blueprints (`community/`)

These blueprints are contributed and maintained by our wonderful open-source community.

| Blueprint                                   | Latest Version | Description                                                              |
| :------------------------------------------ | :------------- | :----------------------------------------------------------------------- |
| [`community/github`](./community/github/)   | `v0.1.0`       | A starter blueprint for the GitHub API, providing basic user lookup.     |
| [`community/spotify`](./community/spotify/) | `v0.1.0`       | Interact with the Spotify Web API to manage playlists, tracks, and more. |

_(This table will grow as the community contributes more blueprints!)_

---

## 🤝 How to Contribute a Blueprint

Contributing a new blueprint is the most valuable way to support the Contextually ecosystem. Our goal is to make this process as simple and automated as possible.

The entire process is managed through the `cx compile` command and GitHub Pull Requests.

### Step 1: Compile Your Blueprint

Find an OpenAPI (or Swagger) specification for the API you want to integrate. Then, use the `cx compile` command to automatically generate the entire blueprint package in your local user namespace.

```bash
# Example for the DigitalOcean API
cx compile https://api.digitalocean.com/v2/openapi.json \
  --name digitalocean \
  --version v1.0.0 \
  --namespace user
```

This command creates a complete blueprint package in your local `~/.cx/blueprints/user/digitalocean/v1.0.0/` directory.

### Step 2: Refine and Test

The compiler does 95% of the work. The final 5% is the human touch:

1.  **Refine `blueprint.cx.yaml`:** Open the generated blueprint file. Your main task is to configure the `supported_auth_methods` section correctly for the API's authentication method.
2.  **Test Locally:** Use `cx connection create` and the interactive shell to create a connection with your new blueprint and test a few of its actions to ensure they work.
3.  **Add a `README.md`:** Create a simple `README.md` inside your new blueprint's directory (e.g., `community/digitalocean/README.md`) explaining what the API is and how to get credentials.

### Step 3: Submit a Pull Request

1.  **Fork this repository** (`flowcontextually/blueprints`) and clone your fork.
2.  **Copy your new blueprint source directory** (e.g., the `digitalocean/` directory) into the `community/` folder of your cloned repository.
3.  **Commit and push** the new files to your fork.
4.  **Open a Pull Request** from your fork back to this repository.

Our team will review your contribution. Once it's merged, we will tag a new release, making your blueprint instantly available to every Contextually user around the world.

---

_Licensed under the MIT License._
