import java.net.InetAddress;
import java.net.UnknownHostException;

public class IPAddressInfo {
    public static void main(String[] args) {
        String ipAddress = "127.0.0.1";

        try{
            InetAddress inetAddress = InetAddress.getByName(ipAddress);

            System.out.println("Ip Address : " +inetAddress.getHostAddress());
            System.out.println("Host Name : " +inetAddress.getHostName());

            if (inetAddress instanceof java.net.Inet4Address){
                System.out.println("Ip Address Type is IPv4 ");
            } else if(inetAddress instanceof java.net.Inet6Address){
                System.out.println("Ip Address Type is IPv6");
            }else {
                System.out.println("Unknown Address Type ");
            }

            byte[] addressBytes=inetAddress.getAddress();
            int firstByte=addressBytes[0] &0xFF;

            if(firstByte>=1&&firstByte<=126){
                System.out.println("Ip Address class : A");
            }else if(firstByte>=127&&firstByte<=191){
                System.out.println("Ip Address class : B");
            }else if(firstByte>=192&&firstByte<=223){
                System.out.println("Ip Address class : C");
            }else if(firstByte>=224&&firstByte<=239){
                System.out.println("Ip Address class : D (Multicast)");
            }else if(firstByte>=240&&firstByte<=255){
                System.out.println("Ip Address class : E (Reserved)");
            }else{
                System.out.println("Unknown Ip Address Class");
            }
        }
        catch (UnknownHostException e){
            e .printStackTrace();
        }
    }
}
