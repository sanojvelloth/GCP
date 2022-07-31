resource "google_compute_instance" "terraform" {
  project      = "project-x-357816"
  name         = "automated"
  machine_type = "n1-standard-1"
  zone         = "us-west1-a"
  boot_disk {
    initialize_params {
      image = "debian-cloud/debian-9"
    }
  }
  network_interface {
    network = "default"
    access_config {
    }
  }
}