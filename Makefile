.PHONY: rust-version format lint test run release all create read update delete

rust-version:
	@echo "Rust command-line utility versions:"
	@rustc --version
	@cargo --version
	@rustfmt --version
	@rustup --version
	@clippy-driver --version

lint:
	@cargo clippy --quiet

test:
	@cargo test --quiet

run:
	@cargo run

release:
	@cargo build --release

all: format lint test run

# CRUD operation targets
create:
	@cargo run -- create

read:
	@cargo run -- read

update:
	@cargo run -- update

delete:
	@cargo run -- delete

extract:
	@cargo run -- extract

load:
	@cargo run -- load
