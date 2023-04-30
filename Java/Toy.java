import java.util.ArrayList;
import java.util.Random;

class Toy {
  String name;
  int ageRange;

  public Toy(String name, int ageRange) {
    this.name = name;
    this.ageRange = ageRange;
  }

  public String getName() {
    return name;
  }

  public int getAgeRange() {
    return ageRange;
  }
}

class Main {
  public static void main(String[] args) {
    ArrayList<Toy> toys = new ArrayList<Toy>();
    toys.add(new Toy("Teddy bear", 2));
    toys.add(new Toy("Legos", 4));
    toys.add(new Toy("Dollhouse", 6));
    toys.add(new Toy("Remote control car", 8));

    Random rand = new Random();
    int index = rand.nextInt(toys.size());
    Toy randomToy = toys.get(index);
    System.out.println("Random toy: " + randomToy.getName() + ", for ages " + randomToy.getAgeRange() + " and up.");
  }
}

