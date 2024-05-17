import java.net.InetAddress;
import java.net.UnknownHostException;
import java.util.Scanner;

public class IPAddressType {

    public static void main(String[] args) {
        try (Scanner scanner = new Scanner(System.in)) {
            System.out.print("Enter the IP Address: ");
            String ipAddress = scanner.next();

            try {
                InetAddress inetAddress = InetAddress.getByName(ipAddress);

                System.out.println("IP Address: " + inetAddress.getHostAddress());
                System.out.println("Class: " + getIPAddressClass(inetAddress));
                System.out.println("Type: " + getIPAddressType(inetAddress));
            } catch (UnknownHostException e) {
                System.out.println("Invalid IP address or hostname");
            }
        }
    }

    private static String getIPAddressClass(InetAddress inetAddress) {
        byte[] addressBytes = inetAddress.getAddress();
        int firstOctet = addressBytes[0] & 0xFF;

        if (firstOctet >= 1 && firstOctet <= 126) {
            return "Class A";
        } else if (firstOctet >= 128 && firstOctet <= 191) {
            return "Class B";
        } else if (firstOctet >= 192 && firstOctet <= 223) {
            return "Class C";
        } else if (firstOctet >= 224 && firstOctet <= 239) {
            return "Class D";
        } else if (firstOctet >= 240 && firstOctet <= 255) {
            return "Class E";
        } else {
            return "Unknown";
        }
    }

    private static String getIPAddressType(InetAddress inetAddress) {
        if (inetAddress.isAnyLocalAddress()) {
            return "Any Local";
        } else if (inetAddress.isLinkLocalAddress()) {
            return "Link Local";
        } else if (inetAddress.isLoopbackAddress()) {
            return "Loopback";
        } else if (inetAddress.isMulticastAddress()) {
            return "Multicast";
        } else if (inetAddress.isSiteLocalAddress()) {
            return "Site Local";
        } else if (inetAddress.isMCGlobal()) {
            return "Multicast Global";
        } else if (inetAddress.isMCNodeLocal()) {
            return "Multicast Node Local";
        } else if (inetAddress.isMCLinkLocal()) {
            return "Multicast Link Local";
        } else if (inetAddress.isMCSiteLocal()) {
            return "Multicast Site Local";
        } else if (inetAddress.isMCOrgLocal()) {
            return "Multicast Organization Local";
        } else {
            return "Public";
}
}
}