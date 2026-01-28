from enum import Enum


class Saml2RequestedAuthnContextConfigurationType0ClassRef(str, Enum):
    AUTHENTICATEDTELEPHONY = "AuthenticatedTelephony"
    INTERNETPROTOCOL = "InternetProtocol"
    INTERNETPROTOCOLPASSWORD = "InternetProtocolPassword"
    KERBEROS = "Kerberos"
    MOBILEONEFACTORCONTRACT = "MobileOneFactorContract"
    MOBILEONEFACTORUNREGISTERED = "MobileOneFactorUnregistered"
    MOBILETWOFACTORCONTRACT = "MobileTwoFactorContract"
    MOBILETWOFACTORUNREGISTERED = "MobileTwoFactorUnregistered"
    NOMADTELEPHONY = "NomadTelephony"
    PASSWORD = "Password"
    PASSWORDPROTECTEDTRANSPORT = "PasswordProtectedTransport"
    PERSONALTELEPHONY = "PersonalTelephony"
    PGP = "PGP"
    PREVIOUSSESSION = "PreviousSession"
    SECUREREMOTEPASSWORD = "SecureRemotePassword"
    SMARTCARD = "Smartcard"
    SMARTCARDPKI = "SmartcardPKI"
    SOFTWAREPKI = "SoftwarePKI"
    SPKI = "SPKI"
    TELEPHONY = "Telephony"
    TIMESYNCTOKEN = "TimeSyncToken"
    TLSCLIENT = "TLSClient"
    UNSPECIFIED = "unspecified"
    X509 = "X509"
    XMLDSIG = "XMLDSig"

    def __str__(self) -> str:
        return str(self.value)
