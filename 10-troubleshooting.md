Trainer:

feature-gate `PodOverhead` must be `true`

- replicas of deployment is 0
- (hard) runtime class has to high podFixed overhead
- image not exist, typo in image name
- (hard) container has not enough resources to start
- wrong start argument
- application version is buggy
- startup probes has to low border
- selector labels on service are wrong
- container port is incorrectly
- service name wrong at ingress
- service port wrong at ingress
- (hidden) v1.0.0 crashed randomly

TODO:

- something with volumes
- configuration error


Tips:

- name ports and reference to them