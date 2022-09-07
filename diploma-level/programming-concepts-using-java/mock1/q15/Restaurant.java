public class Restaurant {
	String[] arr;

	Restaurant(String[] a) {
		arr = a;
	}


	public class Producer {
		String[] buffer;
		Consumer obj;

		Producer() {
			buffer = arr;
		}

		public void produce() {
			if (buffer[0] == null) {
				System.out.println("Consumer has finished consuming");
				return;
			}
			buffer = new String[5];
			for (int i = 0; i < buffer.length; i++) {
				buffer[i] = "Item " + (i + 1);
			}
			System.out.println("Producer has finished producing");
			new Consumer().consume(buffer);
		}
	}


	public class Consumer {
		public void consume(String[] buffer) {
			for (int i = 0; i < buffer.length; i++) {
				buffer[i] = null;
			}
			new Producer().produce();
		}
	}
}