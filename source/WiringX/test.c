#include <stdio.h>

#include "wiringx_dht_read.h"

main() {
	int ret;
	float humidity, temperature;

	ret = wiringx_dht_read(DHT22, 3, &humidity, &temperature);

	printf("%f %f (%d)\n", temperature, humidity, ret);
}
