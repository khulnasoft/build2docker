VERSION=$(shell git rev-parse --short HEAD)
IMAGE_PREFIX=khulnasoft/

build-image:
	docker build -t $(IMAGE_PREFIX)build2docker:v$(VERSION) .

push-image:
	docker push $(IMAGE_PREFIX)build2docker:v$(VERSION)

.all:
	build-image push-image
