use frame_support::{decl_module, dispatch, traits::Get};
use frame_system::ensure_signed;

pub trait Trait: frame_system::Trait {}

decl_module! {
    pub struct Module<T: Trait> for enum Call where origin: T::Origin {
        #[weight = 0]
        pub fn add_patient_record(origin, patient_data: Vec<u8>) -> dispatch::DispatchResult {
            let sender = ensure_signed(origin)?;
            <StorageMap<T::Hash, Vec<u8>> as Store>::insert(patient_record_key, &patient_data);
            Self::deposit_event(Event::PatientRecordAdded(sender, patient_record_key));
            Ok(())
        }

        #[weight = 0]
        pub fn get_patient_record(origin, record_id: T::Hash) -> dispatch::DispatchResult {
            let sender = ensure_signed(origin)?;
            let patient_record = <StorageMap<T::Hash, Vec<u8>> as Store>::get(record_id);
            if patient_record.is_some() {
                Ok(())
            } else {
                Err(DispatchError::Other("Patient record not found"))
            }
        }
    }
}

decl_event! {
    pub enum Event<T> where AccountId = <T as frame_system::Trait>::AccountId {
        PatientRecordAdded(AccountId, T::Hash),
    }
}
